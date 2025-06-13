#!/usr/bin/env python

import time
import rospy
import math
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from actionlib import SimpleActionClient
from niryo_robot_msgs.srv import Trigger, SetInt
from niryo_robot_arm_commander.srv import ComputeTrajectory, ComputeTrajectoryRequest
from geometry_msgs.msg import Pose, Point, Quaternion

class NiryoNed2Client:

    def __init__(self):
        # Client d'action pour le contrôle du bras
        self.client = SimpleActionClient('/niryo_robot_follow_joint_trajectory_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

        # Attendre que le serveur d'action soit prêt
        self.client.wait_for_server()

    def send_goal(self, joint_positions):
        # Créer un objectif de trajectoire pour les joints
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']

        # Ajouter un point de trajectoire avec les positions des jointures et le temps d'exécution
        point = JointTrajectoryPoint()
        point.positions = joint_positions
        point.time_from_start = rospy.Duration(1.0)  # Temps d'exécution du mouvement
        goal.trajectory.points.append(point)

        # Envoyer l'objectif au bras
        rospy.loginfo(f"Sending joint positions: {joint_positions}")
        self.client.send_goal(goal)
        self.client.wait_for_result()

        result = self.client.get_result()
        rospy.loginfo(f"Final result: {result}")

def handle_new_calibration_request():
    rospy.wait_for_service('/niryo_robot/joints_interface/request_new_calibration')
    try:
        calibration_request = rospy.ServiceProxy('/niryo_robot/joints_interface/request_new_calibration', Trigger)
        response = calibration_request()
        rospy.loginfo(f"Calibration request response: {response}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def handle_new_calibration():
    rospy.wait_for_service('/niryo_robot/joints_interface/calibrate_motors')
    try:
        calibration = rospy.ServiceProxy('/niryo_robot/joints_interface/calibrate_motors', SetInt)
        response = calibration(1)
        rospy.loginfo(f"Calibration response: {response}")
        return True
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return False

def handle_calculate_waypoints(pose):
    rospy.wait_for_service('/niryo_robot_arm_commander/compute_waypointed_trajectory')
    try:
        compute_trajectory = rospy.ServiceProxy('/niryo_robot_arm_commander/compute_waypointed_trajectory', ComputeTrajectory)

        # Création d'une demande de trajectoire avec la pose spécifique
        request = ComputeTrajectoryRequest()
        request.list_poses = [pose]  # Utilise la pose passée en paramètre
        request.dist_smoothing = 0
        
        # Appeler le service de calcul de trajectoire
        response = compute_trajectory(request)

        # Vérifier si la trajectoire contient des points
        if response.trajectory.points:
            rospy.loginfo(f"Received trajectory with {len(response.trajectory.points)} points.")
            last_point = response.trajectory.points[-1].positions
            rospy.loginfo(f"Sending final joint positions: {last_point}")
            return last_point
        else:
            rospy.logwarn("Trajectory computation failed or returned no points.")
            return None

    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

if __name__ == '__main__':
    try:
        # Initialisation du nœud ROS
        rospy.init_node('ned2_main_node', anonymous=True)

        # Création d'un client pour le bras Ned2
        ned2_client = NiryoNed2Client()

        # Calibration du robot
        rospy.loginfo("Starting calibration...")
        if handle_new_calibration():
            rospy.loginfo("Calibration complete.")
        else:
            rospy.logerr("Calibration failed.")
            rospy.signal_shutdown("Exiting due to calibration failure.")

        # Définir une liste de poses
        poses = [
            Pose(position=Point(0.2, 0.0, 0.31), orientation=Quaternion(0, math.sqrt(2)/2, 0, math.sqrt(2)/2)),
            Pose(position=Point(0.3, 0.0, 0.35), orientation=Quaternion(0, math.sqrt(2)/2, 0, math.sqrt(2)/2)),
            Pose(position=Point(0.25, -0.1, 0.3), orientation=Quaternion(0, math.sqrt(2)/2, 0, math.sqrt(2)/2)),
        ]

        # Boucle infinie pour répéter les mouvements
        while True:
            for pose in poses:
                rospy.loginfo(f"Calculating waypoints for pose: {pose.position}")
                joint_positions = handle_calculate_waypoints(pose)

                if joint_positions:
                    # Envoi de l'objectif de trajectoire
                    ned2_client.send_goal(joint_positions)
                    time.sleep(2)  # Attendre un peu avant de passer à la pose suivante
                else:
                    rospy.logwarn("No trajectory to send for this pose.")

        # Boucle pour garder le script en exécution si nécessaire
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
