#!/usr/bin/env python3

import rospy
import json
from std_msgs.msg import String, Header
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed

# Publisher global
pub = None

def callback(msg):
    global pub

    try:
        rospy.loginfo("Message reçu : %s", msg.data)

        # Parse JSON
        msg_json = json.loads(msg.data)

        # Création du message JointAnglesWithSpeed
        message = JointAnglesWithSpeed()
        message.joint_names = msg_json["joint_names"]
        print("joint_names",message.joint_names)
        message.joint_angles = msg_json["joint_angles"]
        print("joint_angles",message.joint_angles)
        message.speed = msg_json["speed"]
        print("speed",message.speed)
        message.relative = msg_json["relative"]
        print("relative",message.relative)

        # Création du header
        header_json = msg_json["header"]
        header = Header()
        header.stamp = rospy.Time(
            header_json["stamp"]["sec"],
            header_json["stamp"]["nanosec"]
        )
        header.frame_id = header_json.get("frame_id", "")
        message.header = header
        print("header",message.header)

        # Publication du message
        pub.publish(message)
        rospy.loginfo("Message JointAnglesWithSpeed publié avec succès")

    except Exception as e:
        rospy.logerr("Erreur dans le callback : %s", e)


def relais_subscriber():
    global pub

    rospy.init_node('relais_subscriber', anonymous=True)

    # Initialisation du publisher
    pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)

    # Abonnement au topic '/relais'
    rospy.Subscriber('/relais', String, callback)

    rospy.loginfo("Node 'relais_subscriber' en cours d'exécution. En attente de messages JSON sur /relais...")
    rospy.spin()


if __name__ == '__main__':
    try:
        relais_subscriber()
    except rospy.ROSInterruptException:
        pass
