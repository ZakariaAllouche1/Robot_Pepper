#!/usr/bin/env python3

import rospy
import json
from std_msgs.msg import Header
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
from math import pi
import time



def publier_mouvement(json_test):
    try:
        # Convertir la chaîne JSON en dict Python
        msg_json = json_test 

        # Créer le message ROS
        message = JointAnglesWithSpeed()
        message.joint_names = msg_json["joint_names"]
        message.joint_angles = msg_json["joint_angles"]
        message.speed = msg_json["speed"]
        message.relative = msg_json["relative"]

        # Créer le header
        header_json = msg_json["header"]
        header = Header()
        header.stamp = rospy.Time(
            header_json["stamp"]["sec"],
            header_json["stamp"]["nanosec"]
        )
        header.frame_id = header_json.get("frame_id", "")
        message.header = header

        # Publication
        pub.publish(message)
        rospy.loginfo("✅ Mouvement publié avec succès.")

    except Exception as e:
        rospy.logerr("❌ Erreur lors de la publication : %s", e)

if __name__ == "__main__":
    rospy.init_node("test_mouvement_json")
    pub = rospy.Publisher("/joint_angles", JointAnglesWithSpeed, queue_size=10)

    rospy.sleep(1.0)  # Laisse le temps au publisher de s'initialiser

    now = time.time()
    sec = int(now)
    nanosec = int((now - sec) * 1e9)

######  Mouvement 


    json = {
            "header": {
                "stamp": {
                    "sec": sec,
                    "nanosec": nanosec
                },
                "frame_id": ''
            },
            "joint_names": ["LShoulderRoll","LElbowRoll"],
            "joint_angles": [pi,pi],
            "speed": 0.1,
            "relative": False
    }
    

    pos1_g =  {
        "header": {
            "stamp": {
                "sec": 1749645381,
                "nanosec": 470989563
            },
            "frame_id": ""
        },
        "joint_names": [
             "LShoulderPitch", "LElbowYaw","LElbowRoll"
        ],
        "joint_angles": [
             2.5,-2.5,0.1
        ],
        "speed": 0.1,
        "relative": False
    }

    pos2_g =  {
        "header": {
            "stamp": {
                "sec": 1749645381,
                "nanosec": 470989563
            },
            "frame_id": ""
        },
        "joint_names": [
             "LShoulderPitch", "LElbowYaw","LElbowRoll"
        ],
        "joint_angles": [
             2.5,-2.5,-1.5
        ],
        "speed": 0.1,
        "relative": False
    }

    pos4_g =   {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.9,1,-pi/2,1.2,pi/2,0,0,0,0
                ],
                "speed": 0.1,
                "relative": False}
    
    pos3_g =   {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    2.5,1,-pi/2,1.2,pi/2,0,0,0,0
                ],
                "speed": 0.1,
                "relative": False}
    tete =  {
                    "header": {
                        "stamp": {
                            "sec": 1749645381,
                            "nanosec": 470989563
                        },
                        "frame_id": ""
                    },
                    "joint_names": [
                        "HeadPitch"
                    ],
                    "joint_angles": [
                        0.25
                    ],
                    "speed": 0.1,
                    "relative": False}

    json_init =  {
        "header": {
            "stamp": {
                "sec": 1749645381,
                "nanosec": 470989563
            },
            "frame_id": ""
        },
        "joint_names": [
            "HipPitch", "HipRoll", "KneePitch",
            "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch","LShoulderRoll",
            "LWristYaw","RElbowRoll","RElbowYaw","RHand","RShoulderPitch",
            "RShoulderRoll","RWristYaw"
        ],
        "joint_angles": [
             -0.021475791931152344, -0.015339851379394531, 0.007669, -0.113514, 
             -1.71805, 0.68014, 1.76561, 0.09050, 0.04597, 
             0.10431, 1.70118, 0.67574, 1.739534, -0.0920, -0.026
        ],
        "speed": 0.1,
        "relative": False}

    json_test_maind =  {
        "header": {
            "stamp": {
                "sec": 1749645381,
                "nanosec": 470989563
            },
            "frame_id": ""
        },
        "joint_names": [
             "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch","HipRoll","KneePitch"
        ],
        "joint_angles": [
             0.3,0,-0.7,0.75,0.75,0,-1.2,0.2,0
        ],
        "speed": 0.1,
        "relative": False}

    gobelet_droit=  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RHand","RWristYaw","RElbowRoll","RElbowYaw","RShoulderRoll","HipPitch"
                ],
                "joint_angles": [
                    0.9,1,-pi/2,0.4,pi/2,-0.1,0

                ],
                "speed": 0.1,
                "relative": False}

    gobelet_gauche=  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "LShoulderPitch","LHand","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.9,1,pi/2,-0.4,-pi/2,0,0,0,0
                ],
                "speed": 0.1,
                "relative": False}

    leve_g = {
        "header": {
            "stamp": {
                "sec": 1749645381,
                "nanosec": 470989563
            },
            "frame_id": ""
        },
        "joint_names": [
             "LShoulderPitch","LHand","LWristYaw","LElbowRoll","LElbowYaw","LShoulderRoll","HipPitch","HipRoll","KneePitch"
        ],
        "joint_angles": [
            0.1,1,pi/2,-1.5,-pi/2,0,0,0,0
        ],
        "speed": 0.1,
        "relative": False}

    leve_d =  {
                "header": {
                    "stamp": {
                        "sec": 1749645381,
                        "nanosec": 470989563
                    },
                    "frame_id": ""
                },
                "joint_names": [
                    "RShoulderPitch","RShoulderRoll","RElbowRoll","HipPitch","HipRoll","KneePitch"
                ],
                "joint_angles": [
                    0.1,-0.1,1.3,0,0,0
                ],
                "speed": 0.1,
                "relative": False}
    
    

### Publication des mouvement 
   
    #publier_mouvement(gobelet_droit )
    time.sleep(15)
    publier_mouvement(tete )
    # publier_mouvement(gobelet_gauche
    #  )
    publier_mouvement(json_init)
    
    #publier_mouvement(leve_d)


### Mouvement de la tete pour le launch    

    # time.sleep(15)
    # publier_mouvement(tete )


### Teste mouvement salue
    # for mouv in salue : 

    #     publier_mouvement(mouv)
    #     time.sleep(3)

             #"RShoulderPitch","RElbawRoll"
# "RShoulderPitch","RHand","RWristYaw","RElbowRoll