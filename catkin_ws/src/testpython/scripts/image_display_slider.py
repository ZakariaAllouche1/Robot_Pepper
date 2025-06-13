#!/usr/bin/env python

import sys
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from cv_bridge import CvBridge
import pygame

class ImageDisplay(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.bridge = CvBridge()

        self.image_label = QLabel()

        self.linear_slider = QSlider(Qt.Horizontal)
        self.angular_slider = QSlider(Qt.Horizontal)

        self.linear_slider.setRange(-100, 100)
        self.angular_slider.setRange(-100, 100)
        self.linear_slider.setValue(0)
        self.angular_slider.setValue(0)

        self.linear_slider.valueChanged.connect(self.linear_slider_callback)
        self.angular_slider.valueChanged.connect(self.angular_slider_callback)

        self.timer = QTimer()
        self.timer.timeout.connect(self.publish_cmd_vel)

        self.timer_interval_ms = 100
        self.timer.start(self.timer_interval_ms)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        sliders_layout = QHBoxLayout()
        sliders_layout.addWidget(self.linear_slider)
        sliders_layout.addWidget(self.angular_slider)

        layout.addLayout(sliders_layout)

        self.timer_interval_input = QLineEdit()
        self.timer_interval_input.setPlaceholderText("Timer interval (ms)")
        self.timer_interval_input.textChanged.connect(self.update_timer_interval)

        layout.addWidget(self.timer_interval_input)

        central_widget.setLayout(layout)

        rospy.init_node('image_display_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback)

        pygame.init()
        pygame.joystick.init()
        self.gamepad = None
        if pygame.joystick.get_count() > 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()

        self.gamepad_timer = QTimer()
        self.gamepad_timer.timeout.connect(self.read_gamepad)
        self.gamepad_timer.start(50)  # Read gamepad input every 50 ms




        app.aboutToQuit.connect(self.shutdown)

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Failed to convert image: %s", e)
            return

        height, width, _ = cv_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)

    def linear_slider_callback(self, value):
        self.publish_cmd_vel()

    def angular_slider_callback(self, value):
        self.publish_cmd_vel()

    def publish_cmd_vel(self):
        twist = Twist()
        twist.linear.x = self.linear_slider.value() / 100.0
        twist.angular.z = self.angular_slider.value() / 100.0
        self.cmd_vel_pub.publish(twist)

    def update_timer_interval(self, new_interval):
        try:
            new_interval = int(new_interval)
            if new_interval > 0:
                self.timer_interval_ms = new_interval
                self.timer.start(self.timer_interval_ms)
        except ValueError:
            pass

    def read_gamepad(self):
        if not self.gamepad:
            return

        pygame.event.pump()
        
        # Read the gamepad axes (replace 0 and 1 with the appropriate axis indices for your gamepad)
        linear_value = int(self.gamepad.get_axis(0) * 100)
        angular_value = int(self.gamepad.get_axis(1) * 100)

        # Update the slider values
        self.linear_slider.setValue(linear_value)
        self.angular_slider.setValue(angular_value)



    def shutdown(self):
        rospy.signal_shutdown("Qt application is shutting down")

def main():
    rospy.init_node('image_display_node', anonymous=True)

    app = QApplication(sys.argv)
    window = ImageDisplay(app)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

