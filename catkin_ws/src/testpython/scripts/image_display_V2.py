#!/usr/bin/env python

import sys
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout,QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QSlider, QLineEdit, QSizePolicy, QRadioButton, QButtonGroup 
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from cv_bridge import CvBridge
import pygame

class ImageDisplay(QMainWindow):
    def __init__(self, app):
        super().__init__()
################################################################

        self.gamepad_joy = 1
        self.gamepad_button = 0

    # outerLayout principal pour contenir les images
        outerLayout = QGridLayout()        
        buttonsLayout = QGridLayout()
        slidersLayout = QGridLayout()
        imagesLayout = QGridLayout()
        self.image_labels = []  # Initialize the 'image_labels' attribute as an empty list

    # Créer les étiquettes d'image

        label = QLabel()
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        outerLayout.addWidget(label, 0, 0,2,1)
        self.image_labels.append(label)
        
        
        for i in range(2):
            label = QLabel()
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            imagesLayout.addWidget(label, i, 1)
            self.image_labels.append(label)
 #           outerLayout.setAlignment(label, Qt.AlignHCenter | Qt.AlignVCenter)
            
 #       outerLayout.setColumnStretch(0, 1)
 #       outerLayout.setColumnStretch(1, 1)
        


        # Définition de la hauteur minimale des lignes et de la largeur minimale des colonnes
 #       grid_layout.setRowMinimumHeight(0, 100)
 #       grid_layout.setRowMinimumHeight(1, 100)
 #       grid_layout.setColumnMinimumWidth(0, 150)
 #       grid_layout.setColumnMinimumWidth(1, 150)
        
        
#outerLayout.setColumnMinimumWidth(0, 100)
        outerLayout.setAlignment(Qt.AlignVCenter)

    # Définir la taille de la grande image
        self.image_labels[0].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_labels[0].setMaximumSize(640, 480)

    # Définir la taille des petites images
        self.image_labels[1].setMaximumSize(320, 240)
        self.image_labels[2].setMaximumSize(320, 240)

    # Créer les boutons radio pour sélectionner l'image en grand
        self.groupe_buttons = QButtonGroup()
        self.radio_buttons=[]
        for i in range(3):
            button = QRadioButton("Image " + str(i+1))
            self.radio_buttons.append(button)
            self.groupe_buttons.addButton(button,i+1)   
            buttonsLayout.addWidget(button, i, 0)
        


    # Cocher la première case par défaut
        self.radio_buttons[0].setChecked(True)
 

    # Connecter les boutons radio à la fonction update_large_image
#        for i in range(3):
#            self.radio_buttons[i].clicked.connect(lambda state, x=i: self.update_large_image(x))



################################################################

        self.bridge = CvBridge()

        self.image_label = QLabel()

        self.linear_speed_slider = QSlider(Qt.Horizontal)
        self.angular_speed_slider = QSlider(Qt.Horizontal)

        self.linear_speed_slider.setRange(-100, 100)
        self.angular_speed_slider.setRange(-100, 100)
        self.linear_speed_slider.setValue(0)
        self.angular_speed_slider.setValue(0)

        self.linear_speed_slider.valueChanged.connect(self.linear_speed_slider_callback)
        self.angular_speed_slider.valueChanged.connect(self.angular_speed_slider_callback)

        self.timer = QTimer()
        self.timer.timeout.connect(self.publish_cmd_vel)

        self.timer_interval_ms = 100
        self.timer.start(self.timer_interval_ms)

###############################################################
        self.linear_speed_label = QLabel("Vitesse linéaire")
        self.angular_speed_label = QLabel("Vitesse angulaire")
        self.linear_speed_text = QLineEdit(str(self.linear_speed_slider.value() ))
        self.linear_speed_text.setReadOnly(True)
        self.linear_speed_text.setFixedWidth(50)

        self.angular_speed_text = QLineEdit(str(self.angular_speed_slider.value() ))
        self.angular_speed_text.setFixedWidth(50)
        self.angular_speed_text.setReadOnly(True)


    # Ajouter les contrôles de vitesse au outerLayout
    	
        slidersLayout.addWidget(self.linear_speed_label, 0, 0)
        slidersLayout.addWidget(self.linear_speed_slider, 0, 1)
        slidersLayout.addWidget(self.linear_speed_text, 0, 2)
        slidersLayout.addWidget(self.angular_speed_label, 1, 0)
        slidersLayout.addWidget(self.angular_speed_slider, 1, 1)
        slidersLayout.addWidget(self.angular_speed_text, 1, 2)

        
        outerLayout.addLayout(imagesLayout, 0, 1)  # Ajout de la grille imbriquée dans la cellule (0,0) de la grille principale
        outerLayout.addLayout(buttonsLayout, 2, 0)  # Ajout de la grille imbriquée dans la cellule (2,0) de la grille principale
        outerLayout.addLayout(slidersLayout, 2, 1)  # Ajout de la grille imbriquée dans la cellule (2,1) de la grille principale


        self.timer_interval_input = QLineEdit()
        self.timer_interval_input.setPlaceholderText("Timer interval (ms)")
        self.timer_interval_input.textChanged.connect(self.update_timer_interval)

        slidersLayout.addWidget(self.timer_interval_input)


    # Ajouter le outerLayout principal à la fenêtre
        widget = QWidget()
        widget.setLayout(outerLayout)
        self.setCentralWidget(widget)
        
        rospy.init_node('image_display_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/snpi5/output_video_1', Image, self.image_callback_1)
        rospy.Subscriber('/snpi5/output_video_2', Image, self.image_callback_2)
        rospy.Subscriber('/snpi5/output_video_3', Image, self.image_callback_3)
        
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
        
    def image_callback_1(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Failed to convert image: %s", e)
            return

        height, width, _ = cv_image.shape

        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(qimage)
        id = self.groupe_buttons.checkedId()
        
        if id == 1:
            scaled_pixmap = pixmap.scaled(640,480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.image_labels[0].setPixmap(scaled_pixmap)
        else:
            scaled_pixmap = pixmap.scaled(320,240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            if id == 2:
                self.image_labels[1].setPixmap(scaled_pixmap)
            else:
                self.image_labels[2].setPixmap(scaled_pixmap)
             
       
    def image_callback_2(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Failed to convert image: %s", e)
            return

        height, width, _ = cv_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(qimage)
        id = self.groupe_buttons.checkedId()
        
        if id == 2:
            scaled_pixmap = pixmap.scaled(640,480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.image_labels[0].setPixmap(scaled_pixmap)
        else:
            scaled_pixmap = pixmap.scaled(320,240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_labels[1].setPixmap(scaled_pixmap)


    def image_callback_3(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Failed to convert image: %s", e)
            return

        height, width, _ = cv_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(qimage)
        id = self.groupe_buttons.checkedId()
       
        if id == 3:
            scaled_pixmap = pixmap.scaled(640,480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.image_labels[0].setPixmap(scaled_pixmap)
        else:
            scaled_pixmap = pixmap.scaled(320,240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_labels[2].setPixmap(scaled_pixmap)
 

    def linear_speed_slider_callback(self, value):
        self.publish_cmd_vel()

    def angular_speed_slider_callback(self, value):
        self.publish_cmd_vel()

    def publish_cmd_vel(self):
        twist = Twist()
        twist.linear.x = self.linear_speed_slider.value() / 100.0
        twist.angular.z = self.angular_speed_slider.value() / 100.0

        self.cmd_vel_pub.publish(twist)
       # print(self.

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
        self.linear_speed_slider.setValue(linear_value)
        self.angular_speed_slider.setValue(angular_value)
        formatted_number = f"{linear_value/100:.2f}"
        self.linear_speed_text.setText(formatted_number)
        formatted_number = f"{angular_value/100:.2f}"
        self.angular_speed_text.setText(formatted_number)

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

