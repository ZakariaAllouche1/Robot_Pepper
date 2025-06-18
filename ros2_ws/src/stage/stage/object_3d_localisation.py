#!/usr/bin/env python3
# object_3d_localisation.py

import json

import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from std_msgs.msg import String


class Object3DLocalization(Node):
    def __init__(self) -> None:
        super().__init__('object_3d_localization')

        # 1) Paramétrage dynamique des intrinsics
        self.declare_parameter('fx', 525.0)
        self.declare_parameter('fy', 525.0)
        self.declare_parameter('cx', 320.0)
        self.declare_parameter('cy', 240.0)
        self.fx = self.get_parameter('fx').value
        self.fy = self.get_parameter('fy').value
        self.cx = self.get_parameter('cx').value
        self.cy = self.get_parameter('cy').value

        # 2) CV bridge et stockage de la dernière depth image
        self.bridge = CvBridge()
        self.depth_image = None

        # 3) Subscriptions & Publisher
        self.create_subscription(
            Image,
            '/naoqi_driver/camera/depth/image_raw',
            self._on_depth,
            qos_profile_sensor_data
        )
        self.create_subscription(
            String,
            '/yolo/detections',
            self._on_detections,
            10
        )
        self._pub_objects = self.create_publisher(String, '/objects_3d', 10)

        self.get_logger().info(' Object3DLocalization ready.')

    def _on_depth(self, msg: Image) -> None:
        """Stocke la dernière image de profondeur."""
        try:
            self.depth_image = self.bridge.imgmsg_to_cv2(
                msg, desired_encoding='passthrough'
            )
        except Exception as e:
            self.get_logger().error(f'Depth conversion error: {e}')
            self.depth_image = None

    def _on_detections(self, msg: String) -> None:
        """Convertit 2D detections en positions 3D et publie toujours un JSON."""
        # parse JSON
        try:
            det = json.loads(msg.data)
        except json.JSONDecodeError as e:
            self.get_logger().error(f'Invalid JSON on /yolo/detections: {e}')
            return

        objects_3d = []
        if self.depth_image is not None:
            h, w = self.depth_image.shape[:2]
            for label, center in zip(det.get('labels', []), det.get('centers', [])):
                x_pix, y_pix = center
                if not (0 <= x_pix < w and 0 <= y_pix < h):
                    continue

                z = self.depth_image[y_pix, x_pix]
                # filtre profondeur invalide
                if z == 0 or np.isnan(z):
                    continue
                # mm→m si nécessaire
                if self.depth_image.dtype == np.uint16:
                    z = float(z) / 1000.0
                # reprojection pinhole
                X = (x_pix - self.cx) * z / self.fx
                Y = (y_pix - self.cy) * z / self.fy
                objects_3d.append({'label': label, 'x': X, 'y': Y, 'z': z})

        # publication quel que soit le cas (liste peut être vide)
        out = String()
        out.data = json.dumps(objects_3d)
        # header stamp non disponible sur String, on peut inclure manuellement un timestamp si besoin
        self._pub_objects.publish(out)
        self.get_logger().info(f'→ /objects_3d: published {len(objects_3d)} objects')

def main(args=None) -> None:
    rclpy.init(args=args)
    node = Object3DLocalization()
    try:
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
