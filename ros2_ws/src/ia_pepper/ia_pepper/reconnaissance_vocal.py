import rclpy
from rclpy.node import Node
import sounddevice as sd
import numpy as np
from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import String
import speech_recognition as sr 
from math import pi 


class ReconnaissanceVocal(Node):
    def __init__(self):
        super().__init__('reconnaissance_vocal')

        # Publisher
        self.publisher_ = self.create_publisher(UInt8MultiArray, 'audio_raw', 10)
        self.message = UInt8MultiArray()

        # Index du micro
        self.index_micro = 10 #pour le micro interne de l'ordi

        # Suscriber
        self.subscription = self.create_subscription(String,'retour',self.callback,10)
        self.subscription

    def recup_audio(self):
        """ Fonction qui permet de recuperer la demande vocal et de publier l'audio 
        sur un topic """

        # Creation de l'instance 

        reco = sr.Recognizer()
        mic = sr.Microphone(self.index_micro) 
        
        #Enregistrement 
        with mic as source :
            print("debut enregistrement")
            reco.adjust_for_ambient_noise(source)
            audio = reco.listen(source)
            print("fin de l'enregistrement ")

        # Conversion en fichier wav
        audio_wav = audio.get_wav_data()

        # Publisher 

        self.message.data =  list(audio_wav)
        self.publisher_.publish(self.message)

    def callback(self, msg) : 
        """ Fonction qui capte si un message est arrive pour redeclancher la reconnaissance vocal """
        
        # Relance de la fonction precedente pour la reconnaissance vocal
        self.recup_audio()



def main(args=None):

    
    rclpy.init(args=args)

    node = ReconnaissanceVocal()
    node.recup_audio()
    rclpy.spin(node)
    print("bouh 5")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()
