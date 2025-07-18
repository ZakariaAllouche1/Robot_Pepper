import numpy as np
from math import pi
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8MultiArray, String          
from message_service.srv import Angle, Bouge            
from roboticstoolbox import DHRobot, RevoluteDH
import json                                             
import time


class BougeBras(Node):

    def __init__(self):
        super().__init__('bouge_bras')

        # Subscriber
        self.subscription = self.create_subscription(     # ← renommé (cohérence)
            Int8MultiArray,
            'demande_case_morpion',
            self.callback,
            10,
        )

        # Publisher
        self.publisher_ = self.create_publisher(String, '/relais', 10)
        self.message = String()

        # Client vers le service Angle
        self.cli = self.create_client(Angle, 'angles_pepper')   # ← Angle
        while not self.cli.wait_for_service(1.0):
            self.get_logger().info('service not available, waiting again...')

        # Service « bouge »
        self.service = self.create_service(Bouge, 'bouge', self.callback)  # ← Bouge

    # ------------------------------------------------------------------
    # Cinématique directe (juste passage np.sin / np.cos et @ pour les *
    # ------------------------------------------------------------------
    @staticmethod
    def MGD(q):
        q1, q2, q3, q4, q5, q6 = q
        L1, L2, L3, L4, L5, L6, L7 = (
            0.0936,
            0.0616,
            0.169 - 0.08682,
            0.14974,
            0.1812,
            0.15,
            0.0695,
        )

        T0_1 = np.array(
            [
                [np.cos(q1), -np.sin(q1), 0.0, -L2 * np.cos(q1)],
                [np.sin(q1), np.cos(q1), 0.0, -L2 * np.sin(q1)],
                [0.0, 0.0, 1.0, L1],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T1_2 = np.array(
            [
                [np.cos(q2), -np.sin(q2), 0.0, -L3 * np.cos(q2)],
                [np.sin(q2), np.cos(q2), 0.0, -L3 * np.sin(q2)],
                [0.0, 0.0, 1.0, L4],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T2_3 = np.array(
            [
                [np.cos(q3), -np.sin(q3), 0.0, 0.0],
                [np.sin(q3), np.cos(q3), 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T3_4 = np.array(
            [
                [np.cos(q4), 0.0, np.sin(q4), L5 * np.cos(q4)],
                [np.sin(q4), 0.0, -np.cos(q4), L5 * np.sin(q4)],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T4_5 = np.array(
            [
                [np.cos(q5), 0.0, np.sin(q5), 0.0],
                [np.sin(q5), 0.0, -np.cos(q5), 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T5_6 = np.array(
            [
                [np.cos(q6), 0.0, np.sin(q6), L6 * np.cos(q6)],
                [np.sin(q6), 0.0, -np.cos(q6), L6 * np.sin(q6)],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]
        )

        T0_6 = T0_1 @ T1_2 @ T2_3 @ T3_4 @ T4_5 @ T5_6
        return T0_6[0, 3], T0_6[1, 3], T0_6[2, 3]

    # ------------------------------------------------------------------
    # Jacobienne : juste ajout des virgules manquantes
    # ------------------------------------------------------------------
    def calcule_jacobienn(self, angles):
        L1, L2, L3, L4, L5, L6 = (
            0.0936,
            0.0616,
            0.169 - 0.08682,
            0.14974,
            0.1812,
            0.15,
        )

        robot = DHRobot(
            [
                RevoluteDH(a=-L2, alpha=0, d=L1),
                RevoluteDH(a=-L3, alpha=0, d=L4),
                RevoluteDH(a=0, alpha=pi / 2, d=0),
                RevoluteDH(a=L5, alpha=-pi / 2, d=0),
                RevoluteDH(a=0, alpha=pi / 2, d=0),
                RevoluteDH(a=L6, alpha=-pi / 2, d=0),
            ],
            name='pepper',
        )

        return robot.jacob0(angles)

    # ------------------------------------------------------------------
    # Trajectoire : appels avec self. et np.*
    # ------------------------------------------------------------------
    def trajectoire(self, angles, pos_final):
        q1 = angles[0]
        theta_x = 0
        theta_y = pi / 2
        theta_z = 0

        x, y, z = self.MGD(angles)
        x_init = [x, y, z, theta_x, theta_y, theta_z]

        x_hauteur = np.cos(q1) * 0.2
        y_hauteur = np.sin(q1) * 0.2

        hauteur_att_xr = np.cos(q1) * pos_final[0] + np.sin(q1) * pos_final[1] + 0.2
        dx1 = [hauteur_att_xr * np.cos(q1), -hauteur_att_xr * np.sin(q1), z, theta_x, theta_y, theta_z]
        delta_x_monter = np.linspace(x_init, dx1, 20)

        dx2 = [pos_final[0] + x_hauteur, pos_final[1] + y_hauteur, pos_final[2], theta_x, theta_y, theta_z]
        delta_x_translation = np.linspace(dx1, dx2, 20)

        dx3 = [pos_final[0], pos_final[1], pos_final[2], theta_x, theta_y, theta_z]
        delta_x_descente = np.linspace(dx2, dx3, 20)

        return np.vstack((delta_x_monter, delta_x_translation, delta_x_descente))

    # ------------------------------------------------------------------
    # Calcul de q voulu : création de la requête + correcte
    # ------------------------------------------------------------------
    def calcule_q_voulu(self, X):
        for i in range(1, len(X)):
            # appel service Angle
            req = Angle.Request()                       # ← ajouté
            fut = self.cli.call_async(req)
            rclpy.spin_until_future_complete(self, fut)
            angles = np.array(fut.result().angles)

            # Jacobienne
            J = self.calcule_jacobienn(angles)
            dq = np.linalg.pinv(J[:3, :]) @ (X[i][:3] - X[i - 1][:3])  # diff IK simplifiée
            q_plus_un = angles + dq

            # message de commande
            now = time.time()
            cmd = {
                "header": {"stamp": {"sec": int(now), "nanosec": int((now % 1) * 1e9)}, "frame_id": ""},
                "joint_names": [
                    "HeadPitch",
                    "RShoulderPitch",
                    "RShoulderRoll",
                    "RElbowYaw",
                    "RElbowRoll",
                    "RWristYaw",
                ],
                "joint_angles": q_plus_un.tolist(),
                "speed": 0.1,
                "relative": False,
            }

            self.message.data = json.dumps(cmd)
            self.publisher_.publish(self.message)
            time.sleep(0.05)

    # ------------------------------------------------------------------
    # Callback service : 2 arguments (request, response)
    # ------------------------------------------------------------------
    def callback(self, request, response):
        pos_final = request.position
        req = Angle.Request()
        fut = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, fut)
        angles = np.array(fut.result().angles)

        X = self.trajectoire(angles, pos_final)
        self.calcule_q_voulu(X)

        response.success = True                     # ← renvoyer quelque chose
        return response


def main(args=None):
    rclpy.init(args=args)
    node = BougeBras()                              # ← nom corrigé
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
 