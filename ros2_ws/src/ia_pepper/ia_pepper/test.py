# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Int8MultiArray, String
# import time
# from message_service.srv import Angle
# import numpy as np 
# from math import pi,cos,sin
# from roboticstoolbox import DHRobot, RevoluteDH
# import json 
# import csv


# class Test(Node):
#     def __init__(self):
#         super().__init__('test')

#         # Client vers le service Angle
#         self.cli = self.create_client(Angle, 'Angle')
#         while not self.cli.wait_for_service(timeout_sec=1.0):
#             self.get_logger().info('service not available, waiting again...')

#         # Publisher
#         self.publisher_ = self.create_publisher(String, '/relais', 10)
#         self.message = String()

        
#         self._angle_file = open('angles_traj_calculer.csv', 'w', newline='', encoding='utf-8')
#         self._angle_writer = csv.writer(self._angle_file)
#         # En‑tête (facultative)
#         self._angle_writer.writerow(['x','y','z','q1','q2','q3','q4','q5','q6'])

#     # def MGD(self,q):
#     #     q1, q2, q3, q4, q5, q6 = q
#     #     L1, L2, L3, L4, L5, L6, L7 = (
#     #         0.0936,
#     #         0.0616,
#     #         0.169 - 0.08682,
#     #         0.14974,
#     #         0.1812,
#     #         0.15,
#     #         0.0695,
#     #     )

#     #     T0_1 = np.array(
#     #         [
#     #             [np.cos(q1), -np.sin(q1), 0.0, -L2 * np.cos(q1)],
#     #             [np.sin(q1), np.cos(q1), 0.0, -L2 * np.sin(q1)],
#     #             [0.0, 0.0, 1.0, L1],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]
#     #     )

#     #     T1_2 = np.array(
#     #         [
#     #             [np.cos(q2), -np.sin(q2), 0.0, -L3 * np.cos(q2)],
#     #             [np.sin(q2), np.cos(q2), 0.0, -L3 * np.sin(q2)],
#     #             [0.0, 0.0, 1.0, L4],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]
#     #     )

#     #     T2_3 = np.array(
#     #         [
#     #             [np.cos(q3), -np.sin(q3), 0.0, 0.0],
#     #             [np.sin(q3), np.cos(q3), 0.0, 0.0],
#     #             [0.0, 0.0, 1.0, 0.0],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]
#     #     )

#     #     T3_4 = np.array(
#     #         [
#     #             [np.cos(q4), 0.0, np.sin(q4), L5 * np.cos(q4)],
#     #             [np.sin(q4), 0.0, -np.cos(q4), L5 * np.sin(q4)],
#     #             [0.0, 1.0, 0.0, 0.0],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]   x_pt, y_pt, z_pt = X[i][:3]

    
        
#     #     )

#     #     T4_5 = np.array(
#     #         [
#     #             [np.cos(q5), 0.0, np.sin(q5), 0.0],
#     #             [np.sin(q5), 0.0, -np.cos(q5), 0.0],
#     #             [0.0, 1.0, 0.0, 0.0],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]
#     #     )

#     #     T5_6 = np.array(
#     #         [
#     #             [np.cos(q6), 0.0, np.sin(q6), L6 * np.cos(q6)],
#     #             [np.sin(q6), 0.0, -np.cos(q6), L6 * np.sin(q6)],
#     #             [0.0, 1.0, 0.0, 0.0],
#     #             [0.0, 0.0, 0.0, 1.0],
#     #         ]
#     #     )

#     #     T0_6 = T0_1 @ T1_2 @ T2_3 @ T3_4 @ T4_5 @ T5_6
#     #     return T0_6[0, 3], T0_6[1, 3], T0_6[2, 3]

#     def MGD(self, q):
#         """
#         Cinématique directe bras droit Pepper
#         q : array‑like (6) en radian
#         Renvoie (x, y, z) dans le repère « bouche »
#         """
#         q1, q2, q3, q4, q5, q6 = q
#         L1 = 0.091      # d1  (bouche → ShoulderPitch)
#         L4 = 0.170      # a4  (épaule → coude)
#         L5 = 0.150      # d5  (coude → poignet)
#         L6 = 0.070      # d6  (poignet → paume centre)

#         # Matrices DH successives
#         T01 = np.array([
#             [ np.cos(q1), -np.sin(q1),  0,   0],
#             [ np.sin(q1),  np.cos(q1),  0,   0],
#             [          0,           0,  1,  L1],
#             [          0,           0,  0,   1],
#         ])

#         T12 = np.array([
#             [ np.cos(q2),  0,  np.sin(q2),   0],
#             [ np.sin(q2),  0, -np.cos(q2),   0],
#             [          0,  1,           0,   0],
#             [          0,  0,           0,   1],
#         ])

#         T23 = np.array([
#             [ np.cos(q3),  0, -np.sin(q3),   0],
#             [ np.sin(q3),  0,  np.cos(q3),   0],
#             [          0, -1,           0,   0],
#             [          0,  0,           0,   1],
#         ])

#         T34 = np.array([
#             [ np.cos(q4),  0,  np.sin(q4),  L4*np.cos(q4)],
#             [ np.sin(q4),  0, -np.cos(q4),  L4*np.sin(q4)],
#             [          0,  1,           0,             0],
#             [          0,  0,           0,             1],
#         ])

#         T45 = np.array([
#             [ np.cos(q5), -np.sin(q5), 0,           0],
#             [ np.sin(q5),  np.cos(q5), 0,           0],
#             [          0,           0, 1,          L5],
#             [          0,           0, 0,           1],
#         ])

#         T56 = np.array([
#             [ np.cos(q6), -np.sin(q6), 0,           0],
#             [ np.sin(q6),  np.cos(q6), 0,           0],
#             [          0,           0, 1,          L6],
#             [          0,           0, 0,           1],
#         ])

#         T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
#         x, y, z = T06[0, 3], T06[1, 3], T06[2, 3]
#         return x, y, z


#     def calcule_jacobienn(self, angles):
#         # L1, L2, L3, L4, L5, L6, L7 = (
#         #     0.0936,
#         #     0.0616,
#         #     0.169 - 0.08682,
#         #     0.14974,
#         #     0.1812,
#         #     0.15,
#         #     0.0695,
#         # )

#         L1 = 0.091 # d1  (bouche → ShoulderPitch)
#         L2 =0.
#         L3 = 0.     
#         L4 = 0.170      # a4  (épaule → coude)
#         L5 = 0.150      # d5  (coude → poignet)
#         L6 = 0.070      # d6  (poignet → paume centre)

#         robot = DHRobot(
#             [
#                 RevoluteDH(a=-L2, alpha=0, d=L1),
#                 RevoluteDH(a=-L3, alpha=0, d=L4),
#                 RevoluteDH(a=0, alpha=pi / 2, d=0),
#                 RevoluteDH(a=L5, alpha=-pi / 2, d=0),
#                 RevoluteDH(a=0, alpha=pi / 2, d=0),
#                 RevoluteDH(a=L6, alpha=-pi / 2, d=0),
#             ],
#             name='pepper',
#         )

#         return robot.jacob0(angles)

#     # def trajectoire(self, angles, pos_final):
#     #     q1 = angles[0]
#     #     theta_x = 0
#     #     theta_y = pi / 2
#     #     theta_z = 0

#     #     x, y, z = self.MGD(angles)
#     #     x_init = [x, y, z, theta_x, theta_y, theta_z]

#     #     x_hauteur = np.cos(q1) * 0.2
#     #     y_hauteur = np.sin(q1) * 0.2

#     #     hauteur_att_xr = np.cos(q1) * pos_final[0] + np.sin(q1) * pos_final[1] + 0.2
#     #     dx1 = [hauteur_att_xr * np.cos(q1), -hauteur_att_xr * np.sin(q1), z, theta_x, theta_y, theta_z]
#     #     delta_x_monter = np.linspace(x_init, dx1, 3)

#     #     dx2 = [pos_final[0] + x_hauteur, pos_final[1] + y_hauteur, pos_final[2], theta_x, theta_y, theta_z]
#     #     delta_x_translation = np.linspace(dx1, dx2, 3)

#     #     dx3 = [pos_final[0], pos_final[1], pos_final[2], theta_x, theta_y, theta_z]
#     #     delta_x_descente = np.linspace(dx2, dx3, 3)

#     #     return np.vstack((delta_x_monter, delta_x_translation, delta_x_descente))

#     def trajectoire(self, angles, pos_final,
#                     lift_height: float = 0.15,
#                     n_lift: int = 10,
#                     n_line: int = 10) :
#         """
#         Construit une trajectoire cartésienne en 3 phases :
#         1) lever vertical de `lift_height`
#         2) translation horizontale vers `pos_final`
#         3) descente verticale
#         Renvoie un tableau N×6 (x,y,z,θx,θy,θz).
#         """

#         # orientation fixée (main verticalisée)
#         theta = np.array([0.0, pi / 2, 0.0])

#         # position actuelle
#         x0 = np.array(self.MGD(angles))
#         p0 = np.hstack((x0, theta))

#         # point levé au‑dessus de la position actuelle
#         p_up_start = p0.copy()
#         p_up_start[2] += lift_height

#         # point levé au‑dessus de la cible
#         xT = np.array(pos_final, dtype=float)
#         p_up_goal = np.hstack((xT, theta))
#         p_up_goal[2] += lift_height

#         # point final (au sol)
#         p_goal = np.hstack((xT, theta))

#         # 1) montée
#         seg1 = np.linspace(p0, p_up_start, n_lift, endpoint=False)

#         # 2) translation horizontale
#         seg2 = np.linspace(p_up_start, p_up_goal, n_line, endpoint=False)

#         # 3) descente
#         seg3 = np.linspace(p_up_goal, p_goal, n_lift)

#         vect_final = np.vstack((seg1, seg2, seg3))
        
#         print("Vecteur de trajectoire")
#         print(vect_final)

#         print("pos final :", pos_final)
#         # concaténer, supprimer doublons
#         return vect_final


#     def verif_jacobienne(self, q):
#         eps = 1e-4
#         J_sym = self.calcule_jacobienn(q)[:3, :]
#         J_num = np.zeros_like(J_sym)

#         x0 = np.array(self.MGD(q))
#         for k in range(6):
#             dq = np.zeros(6)
#             dq[k] = eps
#             x1 = np.array(self.MGD(q + dq))
#             J_num[:, k] = (x1 - x0) / eps

#         print("||J_sym - J_num||_max =", np.max(np.abs(J_sym - J_num)))



#     def calcule_q_voulu(self, X):
#         for i in range(1, len(X)):
#             # appel service Angle
#             req = Angle.Request()                       # ← ajouté
#             fut = self.cli.call_async(req)
#             rclpy.spin_until_future_complete(self, fut)
#             angles = np.array(fut.result().angles)

#             # Jacobienne
#             J = self.calcule_jacobienn(angles)
#             # self.verif_jacobienne(angles)
#             dq = np.linalg.pinv(J[:3, :]) @ (X[i][:3] - X[i - 1][:3])  # diff IK simplifiée
#             q_plus_un = angles + dq

#             x_pt, y_pt, z_pt = X[i][:3]

#             # écrire ligne [x,y,z,q1…q6]
#             row = [x_pt, y_pt, z_pt] + q_plus_un.tolist()
#             self._angle_writer.writerow(row)
#             self._angle_file.flush()
#             print("angles calculer :", q_plus_un)
#             # message de commande
#             now = time.time()
#             cmd = {
#                 "header": {"stamp": {"sec": int(now), "nanosec": int((now % 1) * 1e9)}, "frame_id": ""},
#                 "joint_names": [
#                     "HeadPitch",
#                     "RShoulderPitch",
#                     "RShoulderRoll",
#                     "RElbowYaw",
#                     "RElbowRoll",
#                     "RWristYaw",
#                 ],
#                 "joint_angles": q_plus_un.tolist(),
#                 "speed": 0.1,
#                 "relative": False,
#             }

#             self.message.data = json.dumps(cmd)
#             self.publisher_.publish(self.message)
#             time.sleep(3)

#     def test(self):
        
#         pos_final = [0.3250880002539245, -0.1334293922696826,  0.2441435112315246]
#         req = Angle.Request()               
#         future = self.cli.call_async(req)
#         rclpy.spin_until_future_complete(self, future, timeout_sec=5.0)

#         print("angle de depart")
#         if future.done():
#             angles = list(future.result().angles)
#             print(angles)
#         else:
#             self.get_logger().error('Timeout en attendant la réponse Angle')

#         print(" x,y,z de depart")
#         x,y,z = self.MGD(angles)
#         print(f" x :{x}, y :{y}, z: {z}")

#         # print("jacobienne")
#         # jacobienne = self.calcule_jacobienn(angles)
#         # print(jacobienne)

#         X = self.trajectoire(angles,pos_final)

#         self.calcule_q_voulu(X)

#         print("angle d'arriver")
#         req = Angle.Request()               
#         future = self.cli.call_async(req)
#         rclpy.spin_until_future_complete(self, future, timeout_sec=5.0)
#         if future.done():
#             angles = list(future.result().angles)
#             print(angles)
#         else:
#             self.get_logger().error('Timeout en attendant la réponse Angle')

#         print(" x,y,z d'arriver")
#         x,y,z = self.MGD(angles)
#         print(f" x :{x}, y :{y}, z: {z}")

# def main(args=None):
#     rclpy.init(args=args)
#     node = Test()
#     node.test()
#     time.sleep(2)
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()




#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from message_service.srv import Angle
import csv
import time

class AngleLogger(Node):
    def __init__(self):
        super().__init__('angle_logger')
        # Client vers le service Angle
        self.cli = self.create_client(Angle, 'Angle')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Attente du service Angle...')
        # Préparation du fichier CSV
        self._file = open('angles_mouv_morpion.csv', 'w', newline='', encoding='utf-8')
        self._writer = csv.writer(self._file)
        # En‑tête : idx + noms des 6 articulations dans l'ordre de joint_state
        header = [
             
                " HeadYaw",
                "HipPitch",
                "HipRoll",
                "KneePitch",
                "LElbowRoll",
                "LElbowYaw",
                "LHand",
                "LShoulderPitch",
                "LShoulderRoll",
                "LWristYaw",
                "RElbowRoll",
                "RElbowYaw",
                "RHand",
                "RShoulderPitch",
                "RShoulderRoll",
                "RWristYaw"
        ]
        self._writer.writerow(header)
        self._file.flush()

    def log_once(self, idx: int) -> None:
        req = Angle.Request()
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout_sec=2.0)
        if future.done() and future.result() is not None:
            angles = future.result().angles  # array('d', [...])
            # écrire ligne : [idx, q1, q2, q3, q4, q5, q6]
            row = [idx] + list(angles)
            self._writer.writerow(row)
            self._file.flush()
            self.get_logger().info(f'Logged #{idx}: {row[1:]}')
        else:
            self.get_logger().error(f'Échec appel Angle #{idx}')

    def destroy_node(self):
        # Fermer proprement le fichier avant de détruire le node
        self._file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = AngleLogger()
    idx = 1
    try:
        while rclpy.ok():
            node.log_once(idx)
            idx += 1
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
