#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
import math
import time

def joint_state_publisher():
    # Initialize the node
    rospy.init_node('joint_state_publisher')

    # Create a publisher
    # This will publish on the /joint_states topic using the message type JointState
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

    # Set the rate at which to publish the message
    rate = rospy.Rate(10) # 10 Hz

    start_time = time.time()

    while not rospy.is_shutdown():
        # Create a new JointState message
        joint_state = JointState()

        # Set the names of the joints
        joint_state.name = ['axe_1', 'axe_2', 'axe_3']

        # Compute the current time
        current_time = time.time()

        # Compute a sin wave for the current time
        sin_wave = math.sin(current_time - start_time)

        # Set the positions of the joints
        joint_state.position = [sin_wave, sin_wave, sin_wave]

        # Publish the JointState message
        pub.publish(joint_state)

        # Sleep for the remainder of the loop
        rate.sleep()

if __name__ == '__main__':
    try:
        joint_state_publisher()
    except rospy.ROSInterruptException:
        pass
