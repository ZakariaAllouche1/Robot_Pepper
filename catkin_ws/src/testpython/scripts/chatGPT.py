import rospy
from sensor_msgs.msg import JointState
from math import sin, radians

def publish_joint_state():
    rospy.init_node('joint_state_publisher')
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10)  # Taux de publication de 10 Hz (toutes les 10e de seconde)

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        joint_state = JointState()
        joint_state.header.stamp = current_time
        joint_state.name = ['axe_1', 'axe_2', 'axe_3']
        joint_state.position = [radians(30 * sin(2 * 3.14159 * current_time.to_sec()/10.0))] * 3

        pub.publish(joint_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_state()
    except rospy.ROSInterruptException:
        pass
