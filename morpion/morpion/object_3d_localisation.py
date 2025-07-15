#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projette les centres YOLO dans le repère du plateau.
"""

import json, numpy as np, rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Object3DLocalization(Node):
    DET_TOPIC  = '/yolo/detections'
    HOMO_TOPIC = '/board_homography'
    OUT_TOPIC  = '/objects_3d'

    CELL        = 0.07          # côté d’une petite case
    BOARD_HALF  = 0.105         # 0,21 m / 2
    SNAP_THRESH = CELL * np.sqrt(2) * 0.4   # ≃ 0.04 m
    USE_SNAP    = True
    MAX_RANGE   = BOARD_HALF + CELL         # ≃ 0.175 m

    def __init__(self):
        super().__init__('object_3d_localisation')
        self.H=None
        self.create_subscription(String,self.HOMO_TOPIC,self.homo_cb,10)
        self.create_subscription(String,self.DET_TOPIC ,self.dets_cb,10)
        self.pub_3d=self.create_publisher(String,self.OUT_TOPIC,10)
        self.get_logger().info('Object3DLocalization up and running')

    def homo_cb(self,msg:String):
        try:
            h=json.loads(msg.data).get('H',[])
            if len(h)==9:
                self.H=np.asarray(h,np.float32).reshape(3,3)
                self.get_logger().info('Homography loaded')
        except json.JSONDecodeError: pass

    def dets_cb(self,msg:String):
        if self.H is None: return
        try:
            data=json.loads(msg.data)
            labels=data.get('labels',[])
            centers=data.get('centers',[])
        except json.JSONDecodeError: return

        objs=[]
        for lbl,(u,v) in zip(labels,centers):
            if lbl not in ('cup_blue','cup_yellow'): continue
            uv1=np.array([u,v,1.0],np.float32)
            X=self.H@uv1
            if abs(X[2])<1e-6: continue
            x,y=X[0]/X[2],X[1]/X[2]
            if abs(x)>self.MAX_RANGE or abs(y)>self.MAX_RANGE: continue

            # snap
            if self.USE_SNAP:
                cx=round(x/self.CELL)*self.CELL
                cy=round(y/self.CELL)*self.CELL
                if np.hypot(x-cx,y-cy)<self.SNAP_THRESH:
                    x,y=cx,cy

            objs.append({'label':lbl,'x':float(x),'y':float(y),'z':0.0})

        if objs:
            self.pub_3d.publish(String(data=json.dumps(objs)))
            #self.get_logger().info(f"/objects_3d : {objs}")


def main():
    rclpy.init(); rclpy.spin(Object3DLocalization()); rclpy.shutdown()

if __name__=='__main__':
    main()
