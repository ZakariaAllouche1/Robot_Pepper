#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repère les 4 coins du carré rouge (≈ 0,21 m) et publie l’homographie
pixels → coordonnées réelles (x,y).
"""

import math, json, cv2, numpy as np, rclpy
from rclpy.node import Node
from rclpy.qos  import qos_profile_sensor_data
from cv_bridge  import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg    import String


class BoardLocalization(Node):
    RGB_TOPIC  = '/naoqi_driver/camera/bottom/image_raw'
    MASK_TOPIC = '/board_localization/mask'
    HOMO_TOPIC = '/board_homography'

    # --- vision
    LOW_RED1, HIGH_RED1 = np.array([0,100,100]),  np.array([10 ,255,255])
    LOW_RED2, HIGH_RED2 = np.array([160,100,100]), np.array([180,255,255])
    MIN_LINE_LENGTH = 30
    MAX_LINE_GAP    = 7
    BOARD_SIZE      = 0.21          # 21 cm = 3 × 7 cm

    def __init__(self):
        super().__init__('board_localization')
        self.bridge     = CvBridge()
        self.pub_mask   = self.create_publisher(Image , self.MASK_TOPIC, 10)
        self.pub_homo   = self.create_publisher(String, self.HOMO_TOPIC, 10)
        self.board_fixed = False
        self.create_subscription(Image, self.RGB_TOPIC,
                                 self.rgb_cb, qos_profile_sensor_data)
        self.get_logger().info('BoardLocalization started')

    # ---------- RGB callback
    def rgb_cb(self, msg: Image):
        if self.board_fixed:
            return
        bgr  = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        hsv  = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.LOW_RED1, self.HIGH_RED1) | \
               cv2.inRange(hsv, self.LOW_RED2, self.HIGH_RED2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
                                cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
        _, lbl, stats, _ = cv2.connectedComponentsWithStats(mask)
        if stats.shape[0] > 1:
            big = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
            mask = (lbl == big).astype(np.uint8)*255
        self.pub_mask.publish(self.bridge.cv2_to_imgmsg(mask, 'mono8'))

        lines = cv2.HoughLinesP(mask, 1, np.pi/180, 40,
                                self.MIN_LINE_LENGTH, self.MAX_LINE_GAP)
        if lines is None or len(lines) < 4: return

        vert, horz = [], []
        for x1,y1,x2,y2 in lines[:,0]:
            a = abs(math.degrees(math.atan2(y2-y1, x2-x1)))
            a = 180-a if a>90 else a
            (horz if a<15 else vert if a>75 else []).append((x1,y1,x2,y2))
        if len(vert)<2 or len(horz)<2: return
        vert.sort(key=lambda L:(L[0]+L[2])/2)
        horz.sort(key=lambda L:(L[1]+L[3])/2)
        vL,vR = vert[0], vert[-1]
        hT,hB = horz[0], horz[-1]

        def inter(l1,l2):
            x1,y1,x2,y2=l1; x3,y3,x4,y4=l2
            d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
            if abs(d)<1e-6: return None
            px=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d
            py=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d
            return [px,py]

        corners=[inter(vL,hT),inter(vR,hT),inter(vR,hB),inter(vL,hB)]
        if any(c is None for c in corners): return
        pts_img=np.asarray(corners,np.float32)

        # --- coins réels (m)
        d=self.BOARD_SIZE/2.0     # 0,105 m
        pts_real=np.array([[-d, d],[ d, d],[ d,-d],[-d,-d]],np.float32)

        H,_=cv2.findHomography(pts_img,pts_real)
        if H is None: return

        self.pub_homo.publish(String(data=json.dumps({'H':H.flatten().tolist()})))
        self.board_fixed=True
        self.get_logger().info('Homography computed and published')


def main():
    rclpy.init(); rclpy.spin(BoardLocalization()); rclpy.shutdown()

if __name__=='__main__':
    main()
