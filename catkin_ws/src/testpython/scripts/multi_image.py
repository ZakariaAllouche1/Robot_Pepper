#!/usr/bin/env python

import sys
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from cv_bridge import CvBridge
import pygame

class ImageDisplay(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.bridge = CvBridge()

        self.image_labels = [QLabel() for _ in range(3)]
        self.radio_buttons = [QRadioButton(f"Image {i+1}") for i in range(3)]
        self.radio_buttons[0].setChecked(True)

        self.radio_button_group = QButtonGroup()
        for rb in self.radio_buttons:
            self.radio_button_group.addButton(rb)

        self.radio_button_group.buttonClicked.connect(self.update_large_image)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        large_image_layout = QVBoxLayout()
        large_image_layout.addWidget(self.image_labels[0])
        large_image_layout.addWidget(self.radio_buttons[0])

        small_images_layout = QVBoxLayout()
        for i in range(1, 3):
            small_image_layout = QVBoxLayout()
            small_image_layout.addWidget(self.image_labels[i])
            small_image_layout.addWidget(self.radio_buttons[i])
            small_images_layout.addLayout(small_image_layout)

        layout.addLayout(large_image_layout)
        layout.addLayout(small_images_layout)

        sliders_layout = QVBoxLayout()

        # Add the sliders and text fields
        linear_slider = QSlider(Qt.Horizontal)
        angular_slider = QSlider(Qt.Horizontal)
        self.linear_speed_text = QLineEdit('0.0')
        self.angular_speed_text = QLineEdit('0.0')
        
        linear_slider.valueChanged.connect(self.update_linear_speed)
        angular_slider.valueChanged.connect(self.update_angular_speed)

        sliders_layout.addWidget(QLabel("Linear Speed:"))
        sliders_layout.addWidget(linear_slider)
        sliders_layout.addWidget(self.linear_speed_text)
        sliders_layout.addWidget(QLabel("Angular Speed:"))
        sliders_layout.addWidget(angular_slider)
        sliders_layout.addWidget(self.angular_speed_text)

        layout.addLayout(sliders_layout)

        central_widget.setLayout(layout)

        rospy.init_node('image_display_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

 
 #       rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=(0, 1.0))
 #       rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=(1, 0.5))
 #       rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=(2, 0.5))
        
        rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=0)
        rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=1)
        rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback, callback_args=2)



        app.aboutToQuit.connect(self.shutdown)

    def image_callback(self, data, image_index):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
            return

        height, width, bytes_per_component = cv_image.shape
        bytes_per_line = bytes_per_component * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage.rgbSwapped())

        self.image_labels[image_index].setPixmap(pixmap.scaled(self.image_labels[image_index].size(), Qt.KeepAspectRatio))

    def update_large_image(self):
        large_image_index = self.radio_buttons.index(self.radio_button_group.checkedButton())
        small_image_indices = [i for i in range(3) if i != large_image_index]

        self.layout().itemAt(0).addWidget(self.image_labels[large_image_index])
        self.layout().itemAt(1).addWidget(self.image_labels[small_image_indices[0]])
        self.layout().itemAt(2).addWidget(self.image_labels[small_image_indices[1]])

    def update_linear_speed(self, value):
        speed = float(value) / 10.0
        self.linear_speed_text.setText(str(speed))
        self.send_cmd_vel()

    def update_angular_speed(self, value):
        speed = float(value) / 10.0
        self.angular_speed_text.setText(str(speed))
        self.send_cmd_vel()

    def send_cmd_vel(self):
        linear_speed = float(self.linear_speed_text.text())
        angular_speed = float(self.angular_speed_text.text())

        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = angular_speed

        self.cmd_vel_pub.publish(twist)

    def shutdown(self):
        rospy.signal_shutdown("Qt application closed")

def main():
    app = QApplication(sys.argv)
    image_display = ImageDisplay(app)
    image_display.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


