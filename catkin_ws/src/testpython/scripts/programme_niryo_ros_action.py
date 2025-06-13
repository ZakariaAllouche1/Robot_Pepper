#!/usr/bin/env python

import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_robot_to_position():
    # Initialiser le nœud ROS
    rospy.init_node('niryo_robot_joint_trajectory')

    # Créer un client actionlib pour le contrôleur de trajectoire
    client = actionlib.SimpleActionClient(
        '/niryo_robot_follow_joint_trajectory_controller/follow_joint_trajectory',
        FollowJointTrajectoryAction
    )
    
    # Attendre que le serveur soit prêt
    rospy.loginfo("En attente du serveur action...")
    client.wait_for_server()
    rospy.loginfo("Serveur action prêt.")

    # Créer un objectif de trajectoire
    goal = FollowJointTrajectoryGoal()

    # Spécifier les noms des articulations du bras (adapter en fonction de votre robot)
    goal.trajectory.joint_names = [
        'joint_1', 
        'joint_2', 
        'joint_3', 
        'joint_4', 
        'joint_5', 
        'joint_6'
    ]

    # Définir le premier point de trajectoire
    point1 = JointTrajectoryPoint()
    point1.positions = [0.0, -0.5, 1.0, 0.0, 0.5, 0.0]  # Adapter les valeurs en fonction de la position désirée
    point1.time_from_start = rospy.Duration(30.0)  # Temps pour atteindre ce point (3 secondes)

    # Définir le deuxième point de trajectoire
    point2 = JointTrajectoryPoint()
    point2.positions = [0.0, 0.5, -1.0, 0.0, 0.5, 0.0]  # Adapter les valeurs en fonction de la position désirée
    point2.time_from_start = rospy.Duration(60.0)  # Temps pour atteindre ce point après le début de la trajectoire (13 secondes)

    # Ajouter les points à la trajectoire
    goal.trajectory.points.append(point1)
    goal.trajectory.points.append(point2)

    # Envoyer la trajectoire au serveur pour exécution
    rospy.loginfo("Envoi de la trajectoire...")
    client.send_goal(goal)

    # Attendre la fin de l'exécution
    rospy.loginfo("Attente de l'exécution de la trajectoire...")
    client.wait_for_result()
    rospy.loginfo("Trajectoire terminée avec le résultat : %s", client.get_result())

if __name__ == '__main__':
    try:
        move_robot_to_position()
    except rospy.ROSInterruptException:
        rospy.loginfo("Interruption de la commande du robot.")
