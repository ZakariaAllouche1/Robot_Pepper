#!/usr/bin/python
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QVBoxLayout, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from std_msgs.msg import UInt16
from std_msgs.msg import String

import logging
import time
import roslibpy

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
    
        self.client = roslibpy.Ros(host='localhost', port=9090)
        self.client.run()
        
        self.sub1 = roslibpy.Topic(self.client, '/message', 'std_msgs/String')
        self.sub1.subscribe(self.updateLabel7)

        self.pub1 = roslibpy.Topic(self.client, '/threshold/iLowH', 'std_msgs/UInt16')
        self.pub2 = roslibpy.Topic(self.client, '/threshold/iHighH', 'std_msgs/UInt16')
        self.pub3 = roslibpy.Topic(self.client, '/threshold/iLowS', 'std_msgs/UInt16')
        self.pub4 = roslibpy.Topic(self.client, '/threshold/iHighS', 'std_msgs/UInt16')
        self.pub5 = roslibpy.Topic(self.client, '/threshold/iLowV', 'std_msgs/UInt16')
        self.pub6 = roslibpy.Topic(self.client, '/threshold/iHighV', 'std_msgs/UInt16')
            
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()

        vbox = QVBoxLayout()


        sld1 = QSlider(Qt.Horizontal, self)
        sld1.setRange(0, 255)
        sld1.setFocusPolicy(Qt.NoFocus)
        sld1.setPageStep(1)

        sld1.valueChanged.connect(self.updateLabel1)
        
        sld2 = QSlider(Qt.Horizontal, self)
        sld2.setRange(0, 255)
        sld2.setFocusPolicy(Qt.NoFocus)
        sld2.setPageStep(1)

        sld2.valueChanged.connect(self.updateLabel2)

        sld3= QSlider(Qt.Horizontal, self)
        sld3.setRange(0, 255)
        sld3.setFocusPolicy(Qt.NoFocus)
        sld3.setPageStep(1)

        sld3.valueChanged.connect(self.updateLabel3)
        
        sld4 = QSlider(Qt.Horizontal, self)
        sld4.setRange(0, 255)
        sld4.setFocusPolicy(Qt.NoFocus)
        sld4.setPageStep(1)

        sld4.valueChanged.connect(self.updateLabel4)
        
        sld5 = QSlider(Qt.Horizontal, self)
        sld5.setRange(0, 255)
        sld5.setFocusPolicy(Qt.NoFocus)
        sld5.setPageStep(1)

        sld5.valueChanged.connect(self.updateLabel5)
        
        sld6 = QSlider(Qt.Horizontal, self)
        sld6.setRange(0, 255)
        sld6.setFocusPolicy(Qt.NoFocus)
        sld6.setPageStep(1)

        sld6.valueChanged.connect(self.updateLabel6)

        self.label1 = QLabel('0', self)
        self.label1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label1.setMinimumWidth(80)

        self.labeltitle1 = QLabel('iLowH', self)
        self.labeltitle1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle1.setMinimumWidth(80)

        self.label2 = QLabel('0', self)
        self.label2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label2.setMinimumWidth(80)

        self.labeltitle2 = QLabel('iHighH', self)
        self.labeltitle2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle2.setMinimumWidth(80)

        self.label3 = QLabel('0', self)
        self.label3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label3.setMinimumWidth(80)

        self.labeltitle3 = QLabel('iLowS', self)
        self.labeltitle3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle3.setMinimumWidth(80)

        self.label4 = QLabel('0', self)
        self.label4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label4.setMinimumWidth(80)

        self.labeltitle4 = QLabel('iHighS', self)
        self.labeltitle4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle4.setMinimumWidth(80)


        self.label5 = QLabel('0', self)
        self.label5.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label5.setMinimumWidth(80)

        self.labeltitle5 = QLabel('iLowV', self)
        self.labeltitle5.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle5.setMinimumWidth(80)

        self.label6 = QLabel('0', self)
        self.label6.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label6.setMinimumWidth(80)

        self.labeltitle6 = QLabel('iHighV', self)
        self.labeltitle6.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltitle6.setMinimumWidth(80)

        self.label7 = QLabel('Test', self)
        self.label7.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label7.setMinimumWidth(80)

        hbox1.addWidget(self.labeltitle1)
        hbox1.addWidget(sld1)
        hbox1.addWidget(self.label1)

        hbox2.addWidget(self.labeltitle2)
        hbox2.addWidget(sld2)
        hbox2.addWidget(self.label2)

        hbox3.addWidget(self.labeltitle3)
        hbox3.addWidget(sld3)
        hbox3.addWidget(self.label3)
        
        hbox4.addWidget(self.labeltitle4)
        hbox4.addWidget(sld4)
        hbox4.addWidget(self.label4)

        hbox5.addWidget(self.labeltitle5)
        hbox5.addWidget(sld5)
        hbox5.addWidget(self.label5)

        hbox6.addWidget(self.labeltitle6)
        hbox6.addWidget(sld6)
        hbox6.addWidget(self.label6)

        hbox7.addWidget(self.label7)


        self.setLayout(vbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')

        self.show()

    def updateLabel1(self, value):
        self.pub1.publish(roslibpy.Message({'data': value}))
        self.label1.setText(str(value))

    def updateLabel2(self, value):
        self.pub2.publish(roslibpy.Message({'data': value}))
        self.label2.setText(str(value))


    def updateLabel3(self, value):
        self.pub3.publish(roslibpy.Message({'data': value}))
        self.label3.setText(str(value))

    def updateLabel4(self, value):
        self.pub4.publish(roslibpy.Message({'data': value}))
        self.label4.setText(str(value))

    def updateLabel5(self, value):
        self.pub5.publish(roslibpy.Message({'data': value}))
        self.label5.setText(str(value))

    def updateLabel6(self, value):
        self.pub6.publish(roslibpy.Message({'data': value}))
        self.label6.setText(str(value))

    def updateLabel7(self, value):
        toto=value['data']
        self.label7.setText(toto)


    def __del__(self): 
        self.pub1.unadvertise()
        self.pub2.unadvertise()
        self.pub3.unadvertise()
        self.pub4.unadvertise()
        self.pub5.unadvertise()
        self.pub6.unadvertise()
        
        self.sub1.unsubscribe()
        
        self.client.terminate()
        
def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
