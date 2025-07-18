import numpy as np 
from math import pi
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32MultiArray
from message_service.srv import Angle


class RecupAngles(Node):
        def __init__(self):
                super().__init__('recup_angles')

                # Service
                self.service= self.create_service(Angle, 'Angle',self.callback)
                
                # Suscriber
                self.suscriber =  self.create_subscription(JointState, '/joint_states', self.joint_callback, 10)

                # Sauvegarde des dernières positions
                self.dernieres_pos = None
        
  

        def joint_callback(self,msg):
                """ Suscriber qui recuperer a chaque instant les angles des moteurs qui nous interrese
                pour le calcule du MGD et les sauvegarde"""
                
                # # Ajout des positions des moteurs concerner
                # tab = []
                # tab.append(msg.position[1])  # HeadPitch
                # tab.append(msg.position[11]) # RShoulderPitch
                # tab.append(msg.position[12]) # RShoulderRoll
                # tab.append(msg.position[13]) # RElbawYaw
                # tab.append(msg.position[14]) # RElbawRoll
                # tab.append(msg.position[15]) # RWristYaw


                # # Sauvegarde des positions des moteurs qui nous interesse 
                # self.dernieres_pos = tab 
                self.dernieres_pos = msg.position


        def callback(self, request, response):

                """ Service, qui, quand on l'appelle renvoie les angles du robot"""
        
                response.angles =  self.dernieres_pos or []
                return response

       


def main(args=None):

    rclpy.init(args=args)
    node = RecupAngles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

