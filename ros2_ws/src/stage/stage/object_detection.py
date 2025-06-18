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

#         self.get_logger().info(f"YOLOv8 prêt modèle: {model_path}")
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




import cv2, numpy as np, time, json, signal, rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO
from stage.utils.object_recognition import process_detections


class YoloCupNode(Node):
    MODEL_PATH = "yolov8n.pt"
    CONF_YOLO  = 0.10          # on accepte TOUTE bbox cup ≥ 0.10
    PERC_COLOR = 0.40          # 40 % de pixels requis
    LOW_BLUE   = np.array([ 90,  80,  40])
    HIGH_BLUE  = np.array([135, 255, 255])
    LOW_YELLOW = np.array([ 15,  70,  40])
    HIGH_YELLOW= np.array([ 40, 255, 255])

    def __init__(self):
        super().__init__("yolo_cup_node")

        self.model  = YOLO(self.MODEL_PATH)
        self.bridge = CvBridge()
        qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1)

        self.pub_img = self.create_publisher(Image , "/yolo/annotated" , qos)
        self.pub_det = self.create_publisher(String, "/yolo/detections", qos)
        self.sub_img = self.create_subscription(
            Image, "/naoqi_driver/camera/front/image_raw",
            self.image_callback, qos)

        self.get_logger().info(f"✅ YOLOv8 prêt – modèle : {self.MODEL_PATH}")
        signal.signal(signal.SIGINT, lambda *_: rclpy.shutdown())

    # ---------- helpers couleur ----------
    @staticmethod
    def _ratio_mask(hsv, low, high):
        mask = cv2.inRange(hsv, low, high)
        return mask.mean() / 255.0        # proportion de pixels blancs

    # ---------- callback image ----------
    def image_callback(self, msg):
        try:
            bgr = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            self.get_logger().error(f"CV bridge : {e}")
            return

        t0 = time.time()
        res = self.model(bgr, verbose=False, conf=self.CONF_YOLO)[0]
        dt  = (time.time() - t0) * 1000.0

        labels, scores, centers = [], [], []
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

        for box, cls, conf in zip(res.boxes.xyxy.cpu().numpy(),
                                  res.boxes.cls.cpu().numpy(),
                                  res.boxes.conf.cpu().numpy()):

            lbl = self.model.names[int(cls)]
            if lbl != "cup":
                # on garde les autres classes normalement (seuil 0.25 implicite)
                if conf < 0.25:
                    continue
                labels.append(lbl)
                scores.append(float(conf))
                centers.append([int((box[0]+box[2])/2), int((box[1]+box[3])/2)])
                continue

            # ---- cas CUP : filtre couleur ----
            x1,y1,x2,y2 = map(int, box)
            roi = hsv[y1:y2, x1:x2]
            if roi.size == 0:
                continue
            ratio_blue   = self._ratio_mask(roi, self.LOW_BLUE  , self.HIGH_BLUE)
            ratio_yellow = self._ratio_mask(roi, self.LOW_YELLOW, self.HIGH_YELLOW)

            if   ratio_blue   >= self.PERC_COLOR: cup_color = "cup_blue"
            elif ratio_yellow >= self.PERC_COLOR: cup_color = "cup_yellow"
            else:
                continue  # pas assez coloré → rejet

            labels.append(cup_color)
            scores.append(float(conf))
            centers.append([int((x1+x2)/2), int((y1+y2)/2)])

        # -------- publication ----------
        info = process_detections(labels, scores, centers, dt)
        self.pub_det.publish(String(data=json.dumps(info)))

        # annotation pour debug
        for (lbl, c) in zip(labels, centers):
            cv2.putText(bgr, lbl, tuple(c), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0,255,0), 2)
        self.pub_img.publish(self.bridge.cv2_to_imgmsg(bgr, "bgr8"))

        if self.get_clock().now().nanoseconds // 1e9 % 5 == 0:
            self.get_logger().info(f"{len(labels)} dets – {dt:.1f} ms : {labels}")


def main():
    rclpy.init()
    node = YoloCupNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
