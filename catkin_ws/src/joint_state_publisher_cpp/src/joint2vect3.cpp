#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <geometry_msgs/Vector3.h>

class JointToVector3
{
public:
  JointToVector3() : nh_()
  {
    // Initialise Publisher
    pub_ = nh_.advertise<geometry_msgs::Vector3>("consigne", 1);

    // Initialise Subscriber
    sub_ = nh_.subscribe("joint_states", 1, &JointToVector3::callback, this);
  }

  void callback(const sensor_msgs::JointStateConstPtr& msg)
  {
    geometry_msgs::Vector3 vec;

    // Assuming the joints are in the order: axe_1, axe_2, axe_3
    vec.x = msg->position[0];
    vec.y = msg->position[1];
    vec.z = msg->position[2];

    pub_.publish(vec);
  }

private:
  ros::NodeHandle nh_;
  ros::Publisher pub_;
  ros::Subscriber sub_;
};

int main(int argc, char **argv)
{
  ros::init(argc, argv, "joint_to_vector3");

  JointToVector3 jtov;

  ros::spin();

  return 0;
}
