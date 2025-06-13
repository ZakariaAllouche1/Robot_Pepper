import base64
import logging
import time

import roslibpy
import cv2
import numpy as np



# Configure logging
fmt = '%(asctime)s %(levelname)8s: %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

client = roslibpy.Ros(host='127.0.0.1', port=9090)
image_height = 480
image_width = 640
number_of_color_channels = 3

#pixel_array = numpy.full((image_height, image_width, number_of_color_channels), color, dtype=numpy.uint8)

mode = 'BGR'
rgb_copy = np.zeros([640,480,3])

def receive_image(msg):
    log.info('Received image seq=%d', msg['header']['seq'])
    base64_bytes = msg['data'].encode('ascii')
    image_bytes = base64.b64decode(base64_bytes)
    deserialized_bytes = np.frombuffer(image_bytes, dtype=np.uint8)
    img_grayscale = np.reshape(deserialized_bytes, newshape=(480, 640, 3))

 #   img_grayscale =  cv2.cvtColor(img_grayscale,cv2.COLOR_RGB2BGR) 
    cv2.imshow('graycsale image',img_grayscale)
    cv2.waitKey(0)

subscriber = roslibpy.Topic(client, '/cv_camera/image_raw', 'sensor_msgs/Image')
subscriber.subscribe(receive_image)

client.run_forever()
