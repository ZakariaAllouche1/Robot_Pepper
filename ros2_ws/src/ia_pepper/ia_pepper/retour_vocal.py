import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import String
import speech_recognition as sr 


class RetourVocal(Node):
    def __init__(self):
        super().__init__('retour_vocal')

        # Publisher
        self.publisher_ = self.create_publisher(String,'retour', 10)
        self.message = String()
        self.publisher_vocal = self.create_publisher(String,'/speech', 10)
        self.message_vocal = String()
    
        # Suscriber
        self.subscription = self.create_subscription(String,'reponse_ia_texte',self.callback,10)
        self.subscription

    def callback(self,msg):
        """ Fonction qui permet de detecter si le robot à donner sa reponse, envoie sur le topic 
        speech ce que le robot doit dire et publie sur le topic reponse un message pour redeclancher 
        la detection vocal """


        message = msg.data

        print("message recus \n")
        print(message)

        # Envoie du message pour le retour vocal sur Pepper

        # Envoie d'un message pour debloquer la reconnaissance vocal
        self.message.data = 'retour'
        self.publisher_.publish(self.message)

        self.message_vocal.data = msg.data 
        self.publisher_vocal.publish(self.message_vocal)




def main(args=None):
    rclpy.init(args=args)
    node = RetourVocal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()
