#!/usr/bin/env python

import sys
import rospy
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QSlider, QVBoxLayout, QLabel, QWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
from std_msgs.msg import Header

class JointControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_ros()

    def init_ui(self):
        self.setWindowTitle("Joint Control Sliders")

        # Layout principal
        main_layout = QHBoxLayout()

        # Sliders pour le côté gauche
        self.left_sliders = {}
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Left Side Joints"))
        left_joints = {
            'LElbowRoll': -0.4,
            'LElbowYaw': 0.0,
            'LShoulderRoll': 0.5,
            'LShoulderPitch': 0.05
        }
        for joint, default_value in left_joints.items():
            slider = self.create_slider(joint, default_value)
            self.left_sliders[joint] = slider
            left_layout.addWidget(slider)

        # Sliders pour le côté droit
        self.right_sliders = {}
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Right Side Joints"))
        right_joints = {
            'RElbowRoll': 0.5,
            'RElbowYaw': 0.0,
            'RShoulderRoll': -0.5,
            'RShoulderPitch': 0.05
        }
        for joint, default_value in right_joints.items():
            slider = self.create_slider(joint, default_value)
            self.right_sliders[joint] = slider
            right_layout.addWidget(slider)

        # Ajouter les layouts gauche et droit au layout principal
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Configurer le widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Mettre à jour ROS à chaque changement de slider
        for sliders in (self.left_sliders, self.right_sliders):
            for slider in sliders.values():
                slider.valueChanged.connect(self.publish_joint_angles)

    def create_slider(self, joint_name, default_value):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(-100)  # -1.0 * 100
        slider.setMaximum(100)   # 1.0 * 100
        slider.setValue(int(default_value * 100))  # Valeur par défaut
        slider.setToolTip(f"{joint_name}: {default_value}")
        return slider

    def init_ros(self):
        rospy.init_node('joint_control_gui', anonymous=True)
        self.pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=10)

    def publish_joint_angles(self):
        joint_names = []
        joint_angles = []

        # Récupérer les valeurs des sliders gauche
        for joint, slider in self.left_sliders.items():
            joint_names.append(joint)
            joint_angles.append(slider.value() / 100.0)

        # Récupérer les valeurs des sliders droit
        for joint, slider in self.right_sliders.items():
            joint_names.append(joint)
            joint_angles.append(slider.value() / 100.0)

        # Construire et publier le message ROS
        joint_angles_msg = JointAnglesWithSpeed()
        joint_angles_msg.header = Header(seq=0, stamp=rospy.Time.now(), frame_id='')
        joint_angles_msg.joint_names = joint_names
        joint_angles_msg.joint_angles = joint_angles
        joint_angles_msg.speed = 0.1
        joint_angles_msg.relative = False

        self.pub.publish(joint_angles_msg)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = JointControlWindow()
        window.show()
        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
