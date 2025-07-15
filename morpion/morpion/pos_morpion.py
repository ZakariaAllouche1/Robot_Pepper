import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import String
import json 
import time 


class RetourVocal(Node):
    def __init__(self):
        super().__init__('retour_vocal')

        # Publisher
        self.publisher_ = self.create_publisher(String,'/relais', 10)
        #topic de movement fini
        self.pub_done = self.create_publisher(String, '/move_done', 10)
        self.msg_done = String(data='done')
        
    
        # Suscriber
        self.subscription = self.create_subscription(String,'/reponse_case_morpion',self.callback,10)
        self.subscription

    
    def publish_motion(self, mouv: dict, delay: float = 3.0) -> None:
        """Publie la commande JSON puis fait une pause."""
        msg = String()
        msg.data = json.dumps(mouv)
        self.publisher_.publish(msg)
        time.sleep(delay)
        
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

            "C3" :{
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
                    0.85,0,-1.1,0.60,0.7,0,-0.1
                ],
                "speed": 0.1,
                "relative": False},

            "B3" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll"
                ],
                "joint_angles": [
                    0.35,0,-0.9,0.45,0.6,0,-0.7,0.1
                ],
                "speed": 0.1,
                "relative": False},

            "A3" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.,0,-0.9,0.15,0.7,0,-1.3,0.3,-1
                ],
                "speed": 0.2,
                "relative": False},

            "B2" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll"
                ],
                "joint_angles": [
                    0.15,0,-0.6,0.6,0.4,0,-1.0,0.3
                ],
                "speed": 0.1,
                "relative": False},

            "A2" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.03,0,-0.64,0.26,0.5,0,-1.5,0.8,-0.3
                ],
                "speed": 0.1,
                "relative": False},


            "C2" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.3,0,-0.7,1.0,0.5,-0.2,-1.2,0.35,0.5
                ],
                "speed": 0.2,
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


            "C1" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LShoulderPitch","LHand","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch"
                ],
                "joint_angles": [
                    0.85,0,1.1,-0.70,-0.7,0,-0.1
                ],
                "speed": 0.1,
                "relative": False},

            "B1" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LShoulderPitch","LHand","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch"
                ],
                "joint_angles": [
                    0.35,0,0.9,-0.45,-0.6,0,-0.7
                ],
                "speed": 0.1,
                "relative": False},

            "A1" :  {
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
                    0.,0,0.9,-0.15,-0.7,0,-1.3,-0.2,-1
                ],
                "speed": 0.2,
                "relative": False},
                
            "attrape_g": {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LHand"
                ],
                "joint_angles": [
                    0
                ],
                "speed": 0.1,
                "relative": False},

            "leve_g" : {
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
                    0.1,0,pi/2,-1.5,-pi/2,0,0,0,0
                ],
                "speed": 0.1,
                "relative": False},

            "attrape_d" :  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RHand"
                ],
                "joint_angles": [
                    0
                ],
                "speed": 0.1,
                "relative": False},

            "leve_d":  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RShoulderRoll","RElbowRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.1,-0.1,1.3,0,0,0
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
        }


        return mouvement[case]

    def go_gobelet(self,gauche):

        if gauche == True :
            self.publish_motion(self.return_mouv("ferme_main"), 2.)
            self.publish_motion(self.return_mouv("pos3_g"), 1.)
            self.publish_motion(self.return_mouv("pos4_g"), 1.)
            self.publish_motion(self.return_mouv("ouvre_main"), 2.)
            self.publish_motion(self.return_mouv("gobelet_gauche"), 1.)
        
        else :
            self.publish_motion(self.return_mouv("ferme_main"), 2.)
            self.publish_motion(self.return_mouv("pos3_d"), 1.)
            self.publish_motion(self.return_mouv("pos4_d"), 1.)
            self.publish_motion(self.return_mouv("ouvre_main"), 2.)
            self.publish_motion(self.return_mouv("gobelet_droit"), 1.)

    def go_init(self,gauche):

        if gauche == True :
            self.publish_motion(self.return_mouv("gobelet_gauche"), 1.)
            self.publish_motion(self.return_mouv("pos4_g"), 1.)
            self.publish_motion(self.return_mouv("ferme_main"), 2.)
            self.publish_motion(self.return_mouv("pos3_g"), 1.)
            self.publish_motion(self.return_mouv("init"), 1.)
        else:
            self.publish_motion(self.return_mouv("gobelet_droit"), 1.)
            self.publish_motion(self.return_mouv("pos4_d"), 1.)
            self.publish_motion(self.return_mouv("ferme_main"), 2.)
            self.publish_motion(self.return_mouv("pos3_d"), 1.)
            self.publish_motion(self.return_mouv("init"), 1.)


        

    
    
    def callback(self, msg: String) -> None:
        case = msg.data
        self.get_logger().info(f"Case reçue : {case}")

        # Gauche ou droite ?
        is_left = case in ("A1","B1","C1")
        cup_key = "gobelet_gauche" if is_left else "gobelet_droit"
        other_key = "gobelet_droit" if is_left else "gobelet_gauche"

        # 1) Aller au gobelet
        self.go_gobelet(is_left)

        # 2) Attraper + lever
        self.publish_motion(self.return_mouv("attrape_g" if is_left else "attrape_d"))
        self.publish_motion(self.return_mouv("leve_g"    if is_left else "leve_d"))
      

        # 3) Aller à la case
        self.publish_motion(self.return_mouv(case))
        time.sleep(2)

        # 4) Ouvrir la main (relâcher)
        self.publish_motion(self.return_mouv("ouvre_main"))

        # 5) Retour au gobelet
        self.publish_motion(self.return_mouv("leve_g"    if is_left else "leve_d"))
        self.publish_motion(self.return_mouv(cup_key),1.)
       

        # 6) Retour en position initial

        self.go_init(is_left)
        time.sleep(2)
        self.pub_done.publish(self.msg_done)
        self.get_logger().info("Mouvement terminé → /move_done publié")



        # case = msg.data
        # self.get_logger().info(f"Case reçue : {case}")

        # # Gauche ou droite ?
        # is_left = case in ("A1","B1","C1")
        # cup_key = "gobelet_gauche" if is_left else "gobelet_droit"
        # other_key = "gobelet_droit" if is_left else "gobelet_gauche"

        # # 1) Aller au gobelet
        # self.publish_motion(self.return_mouv(cup_key))

        # # 2) Attraper + lever
        # self.publish_motion(self.return_mouv("attrape_g" if is_left else "attrape_d"))
        # self.publish_motion(self.return_mouv("leve_g"    if is_left else "leve_d"))
        # self.publish_motion(self.return_mouv("leve_d"    if is_left else "leve_g"))

        # # 3) Aller à la case
        # self.publish_motion(self.return_mouv(case))
        # time.sleep(2)

        # # 4) Ouvrir la main (relâcher)
        # self.publish_motion(self.return_mouv("ouvre_main"))

        # # 5) Retour au gobelet
        # self.publish_motion(self.return_mouv("leve_g"    if is_left else "leve_d"))
        # self.publish_motion(self.return_mouv("ferme_main"))
        # self.publish_motion(self.return_mouv(cup_key))
        # self.publish_motion(self.return_mouv(other_key))




def main(args=None):
    rclpy.init(args=args)
    node = RetourVocal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()
