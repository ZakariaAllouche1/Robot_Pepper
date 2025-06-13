# import cv2
# import time
# import json
# import signal
# import rclpy
# from rclpy.node import Node
# from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
# from sensor_msgs.msg import Image
# from std_msgs.msg import String
# from cv_bridge import CvBridge
# from ultralytics import YOLO
# from stage.utils.object_recognition import process_detections

# class YoloV8Node(Node):
#     def __init__(self):
#         super().__init__("yolov8_node")

#         self.declare_parameter("model_path", "yolov8n.pt")
#         model_path = self.get_parameter("model_path").value

#         self.model = YOLO(model_path)
#         self.bridge = CvBridge()
#         self.frame_id = 0

#         qos = QoSProfile(
#             reliability=ReliabilityPolicy.RELIABLE,
#             history=HistoryPolicy.KEEP_LAST,
#             depth=1)

#         self.pub_img = self.create_publisher(Image, "/yolo/annotated", qos)
#         self.pub_det = self.create_publisher(String, "/yolo/detections", qos)
#         self.sub_img = self.create_subscription(Image,"/naoqi_driver/camera/front/image_raw",self.image_callback,qos)

#         self.get_logger().info(f"YOLOv8 prêt – modèle: {model_path}")
#         signal.signal(signal.SIGINT, lambda s, f: self._sigint())

#     def image_callback(self, msg):
#         try:
#             frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
#         except Exception as e:
#             self.get_logger().error(f"Conversion échouée : {e}")
#             return

#         t0 = time.time()
#         res = self.model(frame, verbose=False)[0]
#         dt = (time.time() - t0) * 1000.0

#         annotated = res.plot()
#         self.pub_img.publish(self.bridge.cv2_to_imgmsg(annotated, "bgr8"))

#         labels = [self.model.names[int(c)] for c in res.boxes.cls]
#         scores = [round(float(s), 3) for s in res.boxes.conf]
#         centers = []
#         for box in res.boxes.xyxy.cpu().numpy():
#             # box = [xmin, ymin, xmax, ymax]
#             x_center = int((box[0] + box[2]) / 2)
#             y_center = int((box[1] + box[3]) / 2)
#             centers.append([x_center, y_center])

#         detection_info = process_detections(labels, scores, centers, dt)
#         self.pub_det.publish(String(data=json.dumps(detection_info)))

#         self.frame_id += 1
#         if self.frame_id % 20 == 0:
#             self.get_logger().info(
#                 f"[{self.frame_id}] {len(labels)} objs {labels} – {dt:.1f} ms")

#     def _sigint(self):
#         self.get_logger().info("SIGINT reçu, extinction…")
#         rclpy.shutdown()

# def main():
#     rclpy.init()
#     node = YoloV8Node()
#     rclpy.spin(node)
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()



#!/usr/bin/env python3
import os
import cv2
import time
import json
import signal

import numpy as np
import ncnn
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
from ultralytics import YOLO

from stage.utils.object_recognition import process_detections

def nms_np(boxes: np.ndarray, scores: np.ndarray, iou_thr: float):
    """
    Simple NMS NumPy
    boxes: (N,4) x1,y1,x2,y2
    scores: (N,)
    """
    x1, y1, x2, y2 = boxes[:,0], boxes[:,1], boxes[:,2], boxes[:,3]
    areas = (x2 - x1) * (y2 - y1)
    order = scores.argsort()[::-1]
    keep = []
    while order.size:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.clip(xx2 - xx1, 0, None)
        h = np.clip(yy2 - yy1, 0, None)
        inter = w * h
        iou = inter / (areas[i] + areas[order[1:]] - inter)
        order = order[1:][iou < iou_thr]
    return keep

class YoloV8NcnnNode(Node):
    def __init__(self):
        super().__init__("yolov8_ncnn_node")

        # 1) Paramètres modèles
        pkg_share    = get_package_share_directory('stage')
        default_pt    = os.path.join(pkg_share, 'yolov8s_ncnn_model', 'yolov8s.pt')
        default_param = os.path.join(pkg_share, 'yolov8s_ncnn_model', 'yolov8s_opt.param')
        default_bin   = os.path.join(pkg_share, 'yolov8s_ncnn_model', 'yolov8s_opt.bin')

        self.declare_parameter("pt_path",    default_pt)
        self.declare_parameter("param_path", default_param)
        self.declare_parameter("bin_path",   default_bin)
        self.declare_parameter("num_threads", 4)

        pt_path    = self.get_parameter("pt_path").value
        param_path = self.get_parameter("param_path").value
        bin_path   = self.get_parameter("bin_path").value
        num_threads= self.get_parameter("num_threads").value

        # 2) Charge les noms de classes du .pt
        try:
            pt_model = YOLO(pt_path)
            self.class_names = [pt_model.names[i] for i in sorted(pt_model.names.keys())]
        except Exception as e:
            self.get_logger().warn(f"⚠️ Impossible de charger les class_names: {e}")
            self.class_names = []

        # 3) Charge NCNN
        self.net = ncnn.Net()
        self.net.opt.use_vulkan_compute = False
        self.net.opt.num_threads = num_threads

        try:
            self.net.load_param(param_path)
            self.net.load_model(bin_path)
        except Exception as e:
            self.get_logger().error(f"❌ Échec NCNN ({param_path},{bin_path}): {e}")
            raise RuntimeError("Modèle NCNN invalide")

        inp = self.net.input_names()
        out = self.net.output_names()
        if not inp or not out:
            raise RuntimeError("Blobs NCNN non chargés")
        self.get_logger().info(f"NCNN inputs: {inp}, outputs: {out}")
        self.get_logger().info(f"✅ YOLOv8s-NCNN prêt (threads={num_threads})")

        # 4) ROS2 pubs/subs
        self.bridge = CvBridge()
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1)
        self.pub_img = self.create_publisher(Image,  "/yolo/annotated", qos)
        self.pub_det = self.create_publisher(String, "/yolo/detections", qos)
        self.sub_img = self.create_subscription(
            Image,
            "/naoqi_driver/camera/front/image_raw",
            self.image_callback,
            qos)

        self.frame_id = 0
        signal.signal(signal.SIGINT, lambda s,f: self._sigint())

    def yolov8_ncnn_postprocess(self, mats, orig_size,
                                prob_thr=0.25, nms_thr=0.45):
        """
        Décodage des sorties NCNN YOLOv8s
        mats[0] contient tout: (5+nc)×P
        orig_size = (w0,h0)
        """
        w0, h0 = orig_size
        mat = mats[0]
        # charge en numpy
        data = np.frombuffer(mat.data, dtype=np.float32)
        # mat.c = 5+nc, mat.h = P, mat.w = 1
        C = mat.c
        P = mat.h
        preds = data.reshape(C, P).T  # (P, 5+nc)

        # xywh normés, objectness, scores classes
        xywh = preds[:, :4]
        obj  = preds[:, 4]
        cls_scores = preds[:, 5:]
        # score = obj * max_class
        class_ids = np.argmax(cls_scores, axis=1)
        scores = obj * cls_scores[np.arange(P), class_ids]

        mask = scores > prob_thr
        if not mask.any():
            return [], [], []

        xywh = xywh[mask]
        class_ids = class_ids[mask]
        scores = scores[mask]

        # convertit xywh_norm→pixels
        x_c = xywh[:,0] * w0
        y_c = xywh[:,1] * h0
        w   = xywh[:,2] * w0
        h   = xywh[:,3] * h0
        x1 = x_c - w/2
        y1 = y_c - h/2
        x2 = x_c + w/2
        y2 = y_c + h/2
        boxes = np.stack([x1,y1,x2,y2], axis=1)

        # NMS
        keep = nms_np(boxes, scores, nms_thr)
        if not keep:
            return [], [], []

        labels  = [self.class_names[i] for i in class_ids[keep]]
        scoresk = [float(scores[i]) for i in keep]
        centers = [
            (int((boxes[i,0]+boxes[i,2])/2), int((boxes[i,1]+boxes[i,3])/2))
            for i in keep
        ]
        return labels, scoresk, centers

    def image_callback(self, msg):
        # ROS→OpenCV
        try:
            bgr = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f"Conversion échouée : {e}")
            return

        h, w = bgr.shape[:2]
        t0 = time.time()

        # Preproc NCNN
        mat = ncnn.Mat.from_pixels_resize(
            bgr.data, ncnn.Mat.PixelType.PIXEL_BGR2RGB,
            w, h, 640, 640)
        mat.substract_mean_normalize(
            [0.0,0.0,0.0], [1/255.0,1/255.0,1/255.0])

        # Inference
        ex = self.net.create_extractor()
        ex.input(self.net.input_names()[0], mat)
        outputs = []
        for name in self.net.output_names():
            m = ncnn.Mat()
            ex.extract(name, m)
            outputs.append(m)

        dt = (time.time() - t0)*1000

        # Post‐traitement
        labels, scores, centers = self.yolov8_ncnn_postprocess(
            outputs, (w, h), prob_thr=0.25, nms_thr=0.45)

        # Annotate
        annotated = bgr.copy()
        for lbl, scr, (cx, cy) in zip(labels, scores, centers):
            cv2.putText(annotated, f"{lbl} {scr:.2f}",
                        (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0,255,0), 1)

        # Publish
        self.pub_img.publish(self.bridge.cv2_to_imgmsg(annotated, "bgr8"))
        det_info = process_detections(labels, scores, centers, dt)
        self.pub_det.publish(String(data=json.dumps(det_info)))

        self.frame_id += 1
        if self.frame_id % 20 == 0:
            self.get_logger().info(f"[{self.frame_id}] {len(labels)} objs – {dt:.1f} ms")

    def _sigint(self):
        self.get_logger().info("SIGINT reçu, extinction…")
        rclpy.shutdown()


def main():
    rclpy.init()
    try:
        node = YoloV8NcnnNode()
    except RuntimeError:
        return
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
