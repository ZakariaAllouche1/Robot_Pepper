
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
        

    def prompt_VA(self, plateau):
            plateau_vierge = [
                [plateau[0], plateau[1], plateau[2]],
                [plateau[3], plateau[4], plateau[5]],
                [plateau[6], plateau[7], plateau[8]]
            ]

            print(plateau_vierge)
            return f"""
        We are playing tic-tac-toe. You are player 2 (O), and the opponent is player 1 (X).

        The board is a 3x3 grid with rows labeled A, B, C (top to bottom) and columns labeled 1, 2, 3 (left to right).

        Positions are named as Row + Column, for example:
        A1 | A2 | A3
        B1 | B2 | B3
        C1 | C2 | C3


        Each cell can have:
        - 1 = Player 1 (X)
        - 0 = Player 2 (O) (that's you)
        - -1 = empty cell
        with the matrix system for ce board you are : 
            [[A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3]]


        Here is the current board (rows are lists):
        {plateau_vierge}

        Your goal is to select the best move to play (a cell currently empty, i.e., with value -1):
        - to win immediately if possible,
        - if not, to block the opponent's immediate winning move,
        - otherwise to play the best strategic move.

        Only respond with the single name of the cell you want to play (e.g., "B3"). Do not add explanations or any other text.

        #############
        Examples:
        Input board:
        [[1, -1, 1],
        [-1, -1, 1],
        [0, 0, -1]]

        Player 1 (X) has played A1,A3 and C1,
        Player 2 (O) has played C2 and C3.

        Best move: B3

        Input board:
        [[1, -1, -1],
        [-1, 0, 1],
        [1, 0, -1]]
        Player 1 (X) played A1, B3, and C1.
        Player 2 (O) played B2 and B3.
        Best move: A2

        Now, based on the above board, what is your move?
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
                "model": "gemma:2b",
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


