# Dico contenenant les actions que l'ia peut utiliser. 
from math import pi 
import json 
from time import time


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