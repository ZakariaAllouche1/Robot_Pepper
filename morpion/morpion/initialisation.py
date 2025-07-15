import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import String
import json 
import time 


class Initia(Node):
    def __init__(self):
        super().__init__('initia')

        # Publisher
        self.publisher_ = self.create_publisher(String,'/relais', 10)
    

    
    def publish_motion(self, mouv: dict, delay: float = 3.0) -> None:
        """Publie la commande JSON puis fait une pause."""
        msg = String()
        msg.data = json.dumps(mouv)
        self.publisher_.publish(msg)
        time.sleep(delay)

    def go_gobelet(self):

                # self.publish_motion(self.return_mouv("tete"), 1.)
                self.publish_motion(self.return_mouv("pos3_g"), 1.)
                self.publish_motion(self.return_mouv("pos3_d"), 1.)
                self.publish_motion(self.return_mouv("pos4_g"), 1.)
                self.publish_motion(self.return_mouv("pos4_d"), 1.)
                self.publish_motion(self.return_mouv("ouvre_main"), 2.)
                self.publish_motion(self.return_mouv("gobelet_gauche"), 1.)
                self.publish_motion(self.return_mouv("gobelet_droit"), 1.)
             

    def go_init(self):

                self.publish_motion(self.return_mouv("gobelet_gauche"), 1.)
                self.publish_motion(self.return_mouv("gobelet_droit"), 1.)
                self.publish_motion(self.return_mouv("pos4_g"), 1.)
                self.publish_motion(self.return_mouv("pos4_d"), 1.)
                self.publish_motion(self.return_mouv("ferme_main"), 2.)
                self.publish_motion(self.return_mouv("pos3_g"), 2.)
                self.publish_motion(self.return_mouv("pos3_d"), 2.)
                self.publish_motion(self.return_mouv("init"), 2.)

    def return_mouv(self,case):
        pi = np.pi
        mouvement = {


        "gobelet_droit":  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch"
                ],
                "joint_angles": [
                    0.9,1,-pi/2,0.4,pi/2,-0.1,0
                ],
                "speed": 0.1,
                "relative": False},

        "gobelet_gauche":  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LShoulderPitch","LHand","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.9,1,pi/2,-0.4,-pi/2,0,0,0,0
                ],
                "speed": 0.1,
                "relative": False},
            
        "ouvre_main":  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LHand","RHand"
                ],
                "joint_angles": [
                    1,1
                ],
                "speed": 0.1,
                "relative": False},
                
        "init" :   {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "HipPitch", "HipRoll", "KneePitch",
                    "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch","LShoulderRoll",
                    "LWristYaw","RElbowRoll","RElbowYaw","RHand","RShoulderPitch",
                    "RShoulderRoll","RWristYaw"
                ],
                "joint_angles": [
                    -0.021475791931152344, -0.015339851379394531, 0.007669, -0.113514, 
                    -1.71805, 0.68014, 1.76561, 0.09050, 0.04597, 
                    0.10431, 1.70118, 0.67574, 1.739534, -0.0920, -0.026
                ],
                "speed": 0.1,
                "relative": False},

        "pos3_g" :  {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "LShoulderPitch","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch","HipRoll","KneePitch"
                    ],
                    "joint_angles": [
                        2.5,pi/2,-1.2,-pi/2,0,0,0,0
                    ],
                    "speed": 0.1,
                    "relative": False},

        "pos4_g" :   {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "LShoulderPitch","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch","HipRoll","KneePitch"
                    ],
                    "joint_angles": [
                        0.6,pi/2,-1.2,-pi/2,0,0,0,0
                    ],
                    "speed": 0.1,
                    "relative": False},
        "pos3_d" :   {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RShoulderPitch","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                    ],
                    "joint_angles": [
                        2.5,-pi/2,1.2,pi/2,0,0,0,0
                    ],
                    "speed": 0.1,
                    "relative": False},
            
        "pos4_d" :  {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RShoulderPitch","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                    ],
                    "joint_angles": [
                        0.6,-pi/2,1.2,pi/2,0,0,0,0
                    ],
                    "speed": 0.1,
                    "relative": False},

        "tete" :  {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "HeadPitch"
                    ],
                    "joint_angles": [
                        0.25
                    ],
                    "speed": 0.2,
                    "relative": False},
        "ferme_main" :{
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LHand","RHand"
                ],
                "joint_angles": [
                    0,0
                ],
                "speed": 0.1,
                "relative": False},
            }


        return mouvement[case]

    def initialisation(self):
        # mouv = self.return_mouv("tete")
        # msg = String()
        # msg.data = json.dumps(mouv)
        # self.publisher_.publish(msg)
        # time.sleep(1)
        # Aller au gobelet
        self.go_gobelet()
      
        # Temps d'attente pour calibrer
        time.sleep(20)
        # Remise en pose initial
        self.go_init()



def main(args=None):
    rclpy.init(args=args)
    node = Initia()
    node.initialisation()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()