#!/usr/bin/env python
# license removed for brevity
import sys
import rospy
from std_msgs.msg import UInt16
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

class SliderPublisher(QWidget):
    def __init__(self):
        super(SliderPublisher, self).__init__()

        # Initialisation du noeud ROS
        rospy.init_node('slider_publisher', anonymous=True)
        # Changement du nom du topic ici
        self.publisher = rospy.Publisher('/amplitude', UInt16, queue_size=10)

        # Mise en place de l'interface utilisateur
        self.init_ui()

    def init_ui(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setGeometry(30, 40, 100, 30)
        self.slider.setRange(0, 90)
        self.slider.valueChanged[int].connect(self.change_value)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setText(str(self.slider.value()))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.slider)

        self.setLayout(vbox)

    def change_value(self, value):
        self.label.setText(str(value))
        self.publisher.publish(value)

def main():
    app = QApplication(sys.argv)
    ex = SliderPublisher()
    ex.setGeometry(300, 300, 280, 170)
    ex.setWindowTitle('ROS Slider Publisher')
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
