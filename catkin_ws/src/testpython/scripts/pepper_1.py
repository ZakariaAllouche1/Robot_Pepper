#!/usr/bin/env python

import rospy
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
from std_msgs.msg import Header

def publish_joint_angles():
    # Initialiser le noeud ROS
    rospy.init_node('joint_angles_publisher', anonymous=True)

    # Créer un publisher pour le topic /joint_angles
    pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)

    # Définir la fréquence de publication
    rate = rospy.Rate(1)  # 1 Hz

    # Construire le message
    joint_angles_msg = JointAnglesWithSpeed()
    joint_angles_msg.header = Header(seq=0, stamp=rospy.Time.now(), frame_id='')
    joint_angles_msg.joint_names = [
        'KneePitch', 'HipRoll', 'HipPitch', 'RElbowRoll', 'RElbowYaw',
        'RShoulderRoll', 'RShoulderPitch', 'LElbowRoll', 'LElbowYaw',
        'LShoulderRoll', 'LShoulderPitch'
    ]
    joint_angles_msg.joint_angles = [0.2, 0.0, -0.4, 0.5, 0.0, -0.5, 0.05, -0.4, 0.0, 0.5, 0.05]
    joint_angles_msg.speed = 0.1
    joint_angles_msg.relative = False

    rospy.loginfo("Publishing /joint_angles topic...")
    while not rospy.is_shutdown():
        # Mettre à jour le timestamp
        joint_angles_msg.header.stamp = rospy.Time.now()

        # Publier le message
        pub.publish(joint_angles_msg)

        # Attendre le prochain cycle
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_angles()
    except rospy.ROSInterruptException:
        pass
