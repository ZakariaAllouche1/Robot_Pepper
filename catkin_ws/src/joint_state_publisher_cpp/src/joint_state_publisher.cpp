#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <cmath>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "joint_state_publisher_cpp");
    ros::NodeHandle nh;
    ros::Publisher jointStatePub = nh.advertise<sensor_msgs::JointState>("joint_states", 10);
    ros::Rate rate(10);  // Taux de publication de 10 Hz (toutes les 10e de seconde)

    while (ros::ok())
    {
        ros::Time currentTime = ros::Time::now();
        sensor_msgs::JointState jointState;
        jointState.header.stamp = currentTime;
        jointState.name = {"axe_1", "axe_2", "axe_3"};
        double angle = 30.0 * M_PI / 180.0 * sin(2 * M_PI * currentTime.toSec()/20.0);
        jointState.position = {angle, angle, angle};

        jointStatePub.publish(jointState);
        rate.sleep();
    }

    return 0;
}
