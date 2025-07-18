import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import String
import json 
import requests



class MistralMorpion(Node):
    def __init__(self):
        super().__init__('mistral_morpion')

        # Suscriber 
        self.suscription= self.create_subscription(Int8MultiArray, 'demande_case_morpion',self.demande_mistral, 10)
        self.suscription

        # Publisher 
        
        self.publisher = self.create_publisher(String, 'reponse_case_morpion', 10)
        self.message = String()
        

    def cell_symbol(self,val):
        if val == 1:
            return 'X'
        elif val == 0:
            return 'O'
        else:
            return '_'

    def prompt_VA(self, plateau):
        rows = ['A', 'B', 'C']
        board = ""
        for i in range(3):
            line = f"{rows[i]}  [ "
            line += ", ".join(self.cell_symbol(plateau[3*i + j]) for j in range(3))
            line += " ]"
            board += line + "\n"

        return f"""
        You are playing as Player 2 (O). Player 1 (X) is your opponent.

        The tic-tac-toe board uses this format:
            1   2   3
        A [A1, A2, A3]
        B [B1, B2, B3]
        C [C1, C2, C3]

        Each cell contains:
        - X: Player 1 (1)
        - O: Player 2 (0)
        - _: empty (-1)

        Current board state:
        {board}

        Your objective:
        1. If you can win now, do it.
        2. Else, block Player 1 if they can win on the next move.
        3. Otherwise, play the best strategic move.

         Rules:
        - Only respond with the name of the cell to play: A1, B3, C2, etc.
        -  No explanation.
        -  No sentence.
        -  Just the single move (e.g., `B2`) — nothing more.

        If your answer is not a single valid move, it will be rejected.
        """


    def demande_mistral(self, msg):
        """Fonction quienvoie un prompte a la LLM (mistral 7b) et qui renvoie la case à jouer 
        au morpion"""

        print("message reçu")
        print("le plateau est:", msg.data)
        # On recupere le bon prompt avec la requet de l'utilisatuer
        prompt = self.prompt_VA(msg.data)

        # On envoie la demande a la LLM
        reponse = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:7b",
                "prompt": prompt,
                "stream": False
            }
        )

        if reponse.status_code == 200:
            contenu = reponse.json()

            # Extraction du champ "response"
            try:
                texte = contenu["response"].strip()
                self.message.data = texte
                print("Réponse de la LLM :", texte)
            except Exception as e:
                print("Erreur d'extraction :", e)
                self.message.data = "Erreur de parsing réponse"
        else:
            self.message.data = f"Erreur HTTP {reponse.status_code}"


        self.publisher.publish(self.message)
    

def main(args=None):
    print("bouh")
    rclpy.init(args=args)
    node = MistralMorpion()
    rclpy.spin(node)
    print("bouh 2")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


