import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import String
import speech_recognition as sr 
import json 
import time 
from math import pi 

class EnvoieCommande(Node):
    def __init__(self):
        super().__init__('envoie_commande')

        # Publisher
        self.publisher_ = self.create_publisher(String,'/relais', 10)
        self.message = String()
        
    
        # Suscriber
        self.subscription = self.create_subscription(String,'reponse_ia_action',self.callback,10)
        self.subscription

    def callback(self,msg):
        """ Fonction qui permet de detecter si le robot à donner sa reponse, envoie sur le topic 
        speech ce que le robot doit dire et publie sur le topic reponse un message pour redeclancher 
        la detection vocal """

        action_possible = {
                "saluer" : [{
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RElbowRoll","RShoulderPitch","RShoulderRoll"
                    ],
                    "joint_angles": [
                        pi/2,0,-pi/2
                    ],
                    "speed": 0.1,
                    "relative": False
                },
                {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RElbowRoll","RShoulderPitch","RShoulderRoll"
                    ],
                    "joint_angles": [
                        0.8,0,-pi/2
                    ],
                    "speed": 0.1,
                    "relative": False
                },
                {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RElbowRoll","RShoulderPitch","RShoulderRoll"
                    ],
                    "joint_angles": [
                        pi/2,0,-pi/2
                    ],
                    "speed": 0.1,
                    "relative": False
                },

                {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RElbowRoll","RShoulderPitch","RShoulderRoll"
                    ],
                    "joint_angles": [
                        0,pi/2,0
                    ],
                    "speed": 0.1,
                    "relative": False
                }
                ],

                "neutre" : [
                    {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "RElbowRoll","RShoulderPitch","RShoulderRoll", "RElbowRoll","RShoulderPitch","RShoulderRoll"
                    ],
                    "joint_angles": [
                        0,pi/2,0,0,pi/2,0
                    ],
                    "speed": 0.1,
                    "relative": False
                }


                ]




            }

        recup_message = msg.data
        print(recup_message)
        cle = action_possible[f"{recup_message}"]
        for mouv in cle  :
            message = json.dumps(mouv)
            print(message)
            self.message.data = message
            self.publisher_.publish(self.message)
            print("ENVOIE")
            time.sleep(3)
        #message = msg.data

        #print("message recus \n")
        #print(message)

        # Envoie du message pour le retour vocal sur Pepper

        # Envoie d'un message pour debloquer la reconnaissance vocal
        
     

        #self.message = msg.data 
        #self.publisher_(self.message_vocal)




def main(args=None):
    rclpy.init(args=args)
    node = EnvoieCommande()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()
