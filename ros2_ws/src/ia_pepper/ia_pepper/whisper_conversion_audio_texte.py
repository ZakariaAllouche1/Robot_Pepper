import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import torch
import whisper
from std_msgs.msg import UInt8MultiArray
import os
import tempfile



class WhisperNode(Node):
    def __init__(self):
        super().__init__("whisper_node")

        self.subscription = self.create_subscription(UInt8MultiArray,'audio_raw',self.callback,10)
        self.subscription
        self.publisher = self.create_publisher(String,'retranscription', 10)
        self.message = String()

    def callback(self, msg):


        self.get_logger().info(" audio recus ")

        # Chargement du modele small
        model = whisper.load_model("tiny")

        # Reconstituer les bytes
        audio_bytes = bytes(msg.data)

        # Sauvegarder dans un fichier temporaire WAV
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio_bytes)
            audio_temp = f.name
        

        
        #result = model.transcribe(audio_temp,language="fr")
        result = model.transcribe(audio_temp,language="en")


        #result = whisper.decode(self.model, mel, options)
        os.remove(audio_temp)


        # Affichage du texte transcrit
        
        print('\n')
        print({result['text']})

        #publisher 

        self.message.data = result['text']
        self.publisher.publish(self.message)
  





def main(args=None):
    rclpy.init(args=args)
    node = WhisperNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    
    main()
