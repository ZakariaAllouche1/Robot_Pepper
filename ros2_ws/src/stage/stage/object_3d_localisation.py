import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import json
import numpy as np

class Object3DLocalization(Node):
    def __init__(self):
        super().__init__('object_3d_localization')
        self.bridge = CvBridge()
        self.depth_image = None

        # Camera intrinsics params a adapter selon mon robot pepper
        self.fx = 525.0  # focal len x
        self.fy = 525.0  # focal len y
        self.cx = 320.0  # principal point x
        self.cy = 240.0  # principal point y

        self.subscription_depth = self.create_subscription(Image,'/naoqi_driver/camera/depth/image_raw',self.depth_callback,qos_profile_sensor_data)

        self.subscription_det = self.create_subscription(String,'/yolo/detections',self.detections_callback,10)

        self.publisher_3d = self.create_publisher(String, '/objects_3d', 10)

    def depth_callback(self, msg):
        
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")


    def detections_callback(self, msg):
        if self.depth_image is None:
            return

        data = json.loads(msg.data)
        objects_3d = []

        for label, center in zip(data["labels"], data["centers"]):
            x_pixel, y_pixel = center

            if (0 <= y_pixel < self.depth_image.shape[0]) and (0 <= x_pixel < self.depth_image.shape[1]):
                z = self.depth_image[y_pixel, x_pixel]
                if z == 0 or np.isnan(z):  # pas de profondeur fiable
                    continue

                # Si image depth est en uint16 (mm), convertion en metres
                if self.depth_image.dtype == np.uint16:
                    z = z / 1000.0

                # Conversion pixel + profondeur vers coord camera
                X = (x_pixel - self.cx) * z / self.fx
                Y = (y_pixel - self.cy) * z / self.fy
                Z = z

                objects_3d.append({
                    "label": label,
                    "x": float(X),
                    "y": float(Y),
                    "z": float(Z)
                })

        if objects_3d:
            self.publisher_3d.publish(String(data=json.dumps(objects_3d)))

def main(args=None):
    rclpy.init(args=args)
    node = Object3DLocalization()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
