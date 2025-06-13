#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
pub = rospy.Publisher('/niryo_robot_follow_joint_trajectory_controller/command', JointTrajectory, queue_size=10)


def myTestCallback(data):
        rospy.loginfo("I heard %s", data.data)


def myTopicCallback(data):
        rospy.loginfo("I heard %s", data.data)
        join_trajectory = JointTrajectory()
        join_trajectory.header.stamp = rospy.Time.now()
        join_trajectory.joint_names.append("joint_1")
        join_trajectory.joint_names.append("joint_2")
        join_trajectory.joint_names.append("joint_3")
        join_trajectory.joint_names.append("joint_4")
        join_trajectory.joint_names.append("joint_5")
        join_trajectory.joint_names.append("joint_6")
        joint_trajectory_point = JointTrajectoryPoint()
        joint_trajectory_point.time_from_start.secs = 1
        joint_trajectory_point.positions.append(0.4)
        joint_trajectory_point.positions.append(0.2)
        joint_trajectory_point.positions.append(0.0)
        joint_trajectory_point.positions.append(0.1)
        joint_trajectory_point.positions.append(0.3)
        joint_trajectory_point.positions.append(0.0)
        join_trajectory.points.append(joint_trajectory_point)
        pub.publish(join_trajectory)

def my_script():
        rospy.init_node('my_node', anonymous=True)
        rospy.Subscriber("my_topic", String, myTopicCallback)
        rospy.Subscriber("my_test", String, myTestCallback)
        rospy.spin()                                                                     
                                                                                         
if __name__ == '__main__':
        my_script()
