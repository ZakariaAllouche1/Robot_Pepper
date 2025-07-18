import requests
import rclpy
from rclpy.node import Node
import sounddevice as sd
import numpy as np
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String



class DemandeClavier(Node):
    def __init__(self):
        super().__init__('demandeclavier')
        
        self.publisher_ = self.create_publisher(String, 'retranscription', 10)
        self.message = String()

        self.suscription= self.create_subscription(String,'reponse_ia_texte',self.reponse, 10)
        self.suscription

        

    def recup_demande_clavier(self):

        self.message.data = input("Saisissez votre question \n")
        self.publisher_.publish(self.message)

    def reponse(self,msg) : 

        print("message reçus : " )
        print(msg.data)
        self.recup_demande_clavier()
        

def main(args=None):
    
    rclpy.init(args=args)
    node = DemandeClavier()
    
    node.recup_demande_clavier()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
