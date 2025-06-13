#!/usr/bin/env python

import sys
import rospy
from sensor_msgs.msg import Image
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from cv_bridge import CvBridge

class ImageDisplay(QMainWindow):
    def __init__(self, app):
        super().__init__()

        # Initialize the CvBridge
        self.bridge = CvBridge()

        # Create a QLabel to display the image
        self.image_label = QLabel()

        # Create a QWidget and set it as central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout and add the QLabel to it
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        central_widget.setLayout(layout)

        # Initialize ROS subscriber
        rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback)

        # Connect the QApplication aboutToQuit signal to rospy.signal_shutdown
        app.aboutToQuit.connect(self.shutdown)

    def image_callback(self, data):
        try:
            # Convert the ROS image to an OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Failed to convert image: %s", e)
            return

        # Convert the OpenCV image to a QImage
        height, width, _ = cv_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # Convert the QImage to a QPixmap and display it in the QLabel
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)

    def shutdown(self):
        rospy.signal_shutdown("Qt application is shutting down")

def main():
    rospy.init_node('image_display_node', anonymous=True)

    app = QApplication(sys.argv)
    window = ImageDisplay(app)
    window.show()

    # Execute the QApplication and exit the ROS node when the window is closed
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

