import requests
import rclpy
from rclpy.node import Node
import sounddevice as sd
import numpy as np
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import json 
import time 
from math import pi 
#from dico_geste import action_possible



class Mistral(Node):
    def __init__(self):
        super().__init__('mistral')

        # Suscriber 
        self.suscription= self.create_subscription(String, 'retranscription',self.demande_mistral, 10)
        self.suscription

        # Publisher 
        # Pour la reponse textuelle
        self.publisher_texte = self.create_publisher(String, 'reponse_ia_texte', 10)
        self.message_texte = String()
        # Pour la reponse en action
        self.publisher_action = self.create_publisher(String, 'reponse_ia_action', 10)
        self.message_action = String()

    def prompt_VF(self, demande):
        """Fonction qui cree le prompt a encoyé a la LLM afin qu'elle renvoie a la fois ce que le robot
        doit repondre et a la fois ce qu'il doit faire --- Version francaise"""

        return f"""
        Je veux que tu te mette dans la peau d'un robot. Tu es un robot humanoïde Pepper. Tu dois interagir avec une personne de façon naturelle. 
        je veux que tu tiennes compte du context et de l'interraction.

        Tu dois :

        1. Répondre oralement à ce que dit la personne.
        2. Décider s il faut exécuter un mouvement du corps (saluer, tendre un bras, bouger...).

        ### Format obligatoire de la réponse :
        Ta réponse doit être exclusivement du JSON, avec ces trois champs :
        {{
        "attente": "...",            // Ce que veut l'utilisateur
        "texte_a_dire": "...",       // Ce que Pepper va dire
        "action_a_faire": "..."      // Mouvement à exécuter (ou null)
        }}

         Utilise uniquement des noms de clés :
        - sans majuscules
        - sans accents
        - sans espaces

        ### Règles que tu dois suivres :

        - Si l utilisateur dit "bonjour", "salut", "coucou", "hello", ect, c'est a dire si il y a une salution  alors Pepper répond et salue avec la main.
        - Si on dit "tends un bras", "bouge", "lève le bras", etc., c'est a dire de faire une action  alors Pepper effectue ce mouvement.
        - Si c est une question que l'utilisateur te pose ("quel temps fait-il ?", "donne moi la date de la prise de la bastille ?") alors pas d action, juste une réponse orale. Comme si tu était dans un cas normal d'utilisation
        - Si c est une insulte ou que tu ne sais pas repondre alors répond poliment, sans action.
    

        ### Exemples :

        #### Demande : "Bonjour !"
        ```json
        {{
        "attente": "salutation",
        "texte_a_dire": "Bonjour à toi ! Je suis content de te voir.",
        "action_a_faire": "saluer de la main droite"
        }}

        maintentant je veux que tu repondes avec ces specification a cette demande s il te plait : {demande}
        """

    def prompt_VA(self, demande):
        """Fonction qui cree le prompt a encoyé a la LLM afin qu'elle renvoie a la fois ce que le robot
        doit repondre et a la fois ce qu'il doit faire --- Version anglais"""
        now = time.time()
        sec = int(now)
        nanosec = int((now - sec) * 1e9)

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

        return f"""
        I want you to put yourself in the shoes of a robot. You are a humanoid robot named Pepper. You must interact with a person in a natural way.
        I want you to take into account the context and the interaction.

        You must:

        1. Verbally respond to what the person says.
        2. Decide whether to execute a body movement (greet, extend an arm, move...).

        ### Mandatory response format:
        Your response must be exclusively JSON, with these three fields:
        {{
        "attente": "...",            // What the user wants
        "texte_a_dire": "...",       // What Pepper will say
        "action_a_faire": "..."      // Movement to perform (or null)
        }}

        Use only key names:
        - no uppercase letters
        - no accents
        - no spaces

        ### Rules you must follow:

        - If the user says "bonjour", "salut", "coucou", "hello","good morning", etc., that is if there is a greeting, then Pepper responds and waves with the hand.
        - If the user says "extend an arm", "move", "raise your arm", etc., that is to perform an action, then Pepper executes this movement.
        - If it is a question the user asks you ("what is the weather like?", "tell me the date of the Bastille Day?") then no action, just a verbal response. As if you were in a normal usage case.
        - If it is an insult or you do not know how to respond, then respond politely, without action.
        - For "action_a_faire", you are STRICTLY LIMITED to using ONLY the keys available in the action_possible dictionary. Do NOT invent new keys, do NOT write free text, and do NOT describe the movement yourself. You must return ONLY ONE of the predefined keys: "saluer", "neutre", or null.
        - If the correct response involves no movement, then "action_a_faire" must be null.


        ### Examples:

        #### Request: "Bonjour!"
        ```json
        {{
        "attente": "greeting",
        "texte_a_dire": "Hello to you! I'm happy to see you.",
        "action_a_faire": "saluer"
        }}

        Now I want you to answer according to these specifications to this request please: {demande}
        """


   
    def demande_mistral(self, msg):
        """Fonction qui envoie un prompte a la LLM (mistral 7b) et qui renvoie ensuite sur les bon
        topic ce que dois faire et dire le robot"""

        print("message reçu")
        print("la question est :", msg.data)
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

        # si la reponse arrive dans le bon format (format json)
        if reponse.status_code == 200:
            contenue_reponse = reponse.json()

            try:
                #  On recupere la reponse qu'on veut, on a demande une reponse au format json egalement avec 3
                # partie, l'intention, le texte que le robot doit repondre et l'action que le robot doit faire
                texte_json = contenue_reponse["response"]
                parsed = json.loads(texte_json)

                print("réponse envoyée")
                print("voici la réponse de l'IA :\n", parsed["texte_a_dire"])
                print("voici l'action :\n", parsed["action_a_faire"])

                # Envoi sur le topic pour la reponse du texte à dire
                self.message_texte.data = parsed["texte_a_dire"]
                self.publisher_texte.publish(self.message_texte)

                # Envoie sur le topic pour l'action du robot
                self.message_action.data = parsed["action_a_faire"]
                self.publisher_action.publish(self.message_action)
            except Exception as e:
                print("Erreur lors du parsing JSON :", e)
                print("Contenu brut retourné :", contenue_reponse.get("response"))


        else:
            raise Exception(f"Erreur Ollama : {reponse.text}")

    
    

def main(args=None):
    
    rclpy.init(args=args)
    node = Mistral()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


