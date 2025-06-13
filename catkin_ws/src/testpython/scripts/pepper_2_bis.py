#!/usr/bin/env python

import sys
import rospy
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QSlider, QVBoxLayout, QLabel, QWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


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
        self.left_joints = {
            'LShoulderPitch': 0.05, 'LShoulderRoll': 0.5,
            'LElbowYaw': 0.0, 'LElbowRoll': -0.4, 'LWristYaw': 0.0
        }
        for joint, default_value in self.left_joints.items():
            slider = self.create_slider(joint, default_value)
            self.left_sliders[joint] = slider
            left_layout.addWidget(slider)

        # Sliders pour le côté droit
        self.right_sliders = {}
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Right Side Joints"))
        self.right_joints = {
            'RShoulderPitch': 0.05, 'RShoulderRoll': -0.5,
            'RElbowYaw': 0.0, 'RElbowRoll': 0.5, 'RWristYaw': 0.0
        }
        for joint, default_value in self.right_joints.items():
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
                slider.valueChanged.connect(self.publish_joint_trajectories)

    def create_slider(self, joint_name, default_value):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(-100)  # -1.0 * 100
        slider.setMaximum(100)   # 1.0 * 100
        slider.setValue(int(default_value * 100))  # Valeur par défaut
        slider.setToolTip(f"{joint_name}: {default_value}")
        return slider

    def init_ros(self):
        rospy.init_node('joint_control_gui', anonymous=True)

        # Publishers pour les contrôleurs
        self.left_arm_pub = rospy.Publisher(
            '/pepper_dcm/LeftArm_controller/command', JointTrajectory, queue_size=10)
        self.right_arm_pub = rospy.Publisher(
            '/pepper_dcm/RightArm_controller/command', JointTrajectory, queue_size=10)

    def create_trajectory(self, joint_names, positions, duration=2.0):
        trajectory = JointTrajectory()
        trajectory.joint_names = joint_names
        point = JointTrajectoryPoint()
        point.positions = positions
        point.velocities = [0.1] * len(positions)  # Vitesses facultatives
        point.time_from_start = rospy.Duration(duration)
        trajectory.points.append(point)
        trajectory.header.stamp = rospy.Time.now()
        return trajectory

    def publish_joint_trajectories(self):
        # Construire les trajectoires pour le bras gauche
        left_positions = [self.left_sliders[joint].value() / 100.0 for joint in self.left_joints.keys()]
        left_trajectory = self.create_trajectory(list(self.left_joints.keys()), left_positions)

        # Construire les trajectoires pour le bras droit
        right_positions = [self.right_sliders[joint].value() / 100.0 for joint in self.right_joints.keys()]
        right_trajectory = self.create_trajectory(list(self.right_joints.keys()), right_positions)

        # Publier sur les contrôleurs respectifs
        self.left_arm_pub.publish(left_trajectory)
        self.right_arm_pub.publish(right_trajectory)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = JointControlWindow()
        window.show()
        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
