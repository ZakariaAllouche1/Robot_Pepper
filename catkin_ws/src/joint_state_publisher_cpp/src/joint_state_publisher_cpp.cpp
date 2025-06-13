#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <cmath>

class Trajectoire {
public:
  Trajectoire() : nh_(""), jointStatePub_(nh_.advertise<sensor_msgs::JointState>("joint_states", 10)) {
    jointState_.name = {"axe_1", "axe_2", "axe_3"};
  }

  void run() {
    ros::Rate rate(10);  // Taux de publication de 10 Hz (toutes les 10e de seconde)
    while (ros::ok()) {
      updateJointState();
      publishJointState();
      rate.sleep();
    }
  }

private:
  ros::NodeHandle nh_;
  ros::Publisher jointStatePub_;
  sensor_msgs::JointState jointState_;

  void updateJointState() {
    ros::Time currentTime = ros::Time::now();
    double angle = 30.0 * M_PI / 180.0 * sin(2 * M_PI * currentTime.toSec()/20.0);
    jointState_.header.stamp = currentTime;
    jointState_.position = {angle, angle, angle};
  }

  void publishJointState() {
    jointStatePub_.publish(jointState_);
  }
};

int main(int argc, char** argv) {
  ros::init(argc, argv, "joint_state_publisher_cpp");

  Trajectoire trajectoire;
  trajectoire.run();

  return 0;
}
