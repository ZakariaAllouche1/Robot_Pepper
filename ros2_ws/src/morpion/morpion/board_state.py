#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construit la grille logique 3×3 à partir de /objects_3d.
"""

import json, numpy as np, rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BoardState(Node):
    OBJECTS_TOPIC = '/objects_3d'
    STATE_TOPIC   = '/tic_tac_state'

    CELL    = 0.07             
    TH_DIST = CELL * 0.55    

    def __init__(self):
        super().__init__('board_state')
        # centres des neuf cases (y positif = rangée la plus éloignée)
        c=[-self.CELL,0.0,self.CELL]
        self.centres=[(x,y) for y in c[::-1] for x in c]

        self.create_subscription(String,self.OBJECTS_TOPIC,self.cb_objs,10)
        self.pub_state=self.create_publisher(String,self.STATE_TOPIC,10)
        self.last_board=None
        self.get_logger().info('BoardState ready')

    def cb_objs(self,msg:String):
        try: objs=json.loads(msg.data)
        except json.JSONDecodeError: return
        if not isinstance(objs,list): return

        board=[['' for _ in range(3)] for _ in range(3)]
        for o in objs:
            lbl=o.get('label','')
            if lbl not in ('cup_blue','cup_yellow'): continue
            x,y=o['x'],o['y']
            dists=[np.hypot(x-cx,y-cy) for cx,cy in self.centres]
            idx=int(np.argmin(dists))
            if dists[idx]>self.TH_DIST: continue
            row,col=divmod(idx,3)
            if not board[row][col]:
                board[row][col]='blue' if 'blue' in lbl else 'yellow'

        if board!=self.last_board:
            self.pub_state.publish(String(data=json.dumps({'board':board})))
            self.get_logger().info(f'Board state : {board}')
            self.last_board=board


def main():
    rclpy.init(); rclpy.spin(BoardState()); rclpy.shutdown()

if __name__=='__main__':
    main()
