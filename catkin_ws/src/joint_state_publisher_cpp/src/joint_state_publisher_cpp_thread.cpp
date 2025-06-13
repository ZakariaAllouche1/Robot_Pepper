#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <signal.h>
#include <thread>

    static void monsigintHandler(int sig) {
        ROS_INFO("Ctrl+C detected. Shutting down...");
        ros::shutdown();
    }



class SinusoidalTrajectory {
public:
    SinusoidalTrajectory() : amplitude(30 * M_PI / 180), period(20.0), frequency(1.0 / period) {
        // Publisher for joint states
        pub = n.advertise<sensor_msgs::JointState>("joint_states", 10);
        
        // Launch the thread for generating and publishing joint states
        jointStateThread = std::thread(&SinusoidalTrajectory::generateAndPublishJointStates, this);
    }

    ~SinusoidalTrajectory() {
        // Wait for the joint state thread to finish
        jointStateThread.join();
    }

    // Handler for Ctrl+C
    static void sigintHandler(int sig) {
        ROS_INFO("Ctrl+C detected. Shutting down...");
        ros::shutdown();
    }

    // Thread function for generating and publishing sinusoidal joint states
    void generateAndPublishJointStates() {
        ros::Rate loop_rate(10); // 10 Hz
        sensor_msgs::JointState js;
        js.name.push_back("axe_1");
        js.name.push_back("axe_2");
        js.name.push_back("axe_3");
        js.position.resize(3);

        double t = 0.0;

        while (ros::ok()) {
            // Generate sinusoidal joint position
            for(int i = 0; i < 3; ++i) {
                js.position[i] = amplitude * sin(2 * M_PI * frequency * t);
            }
            js.header.stamp = ros::Time::now();
            pub.publish(js);
            
            loop_rate.sleep();
            t += 0.1;
        }
    }

private:
    double amplitude;
    double period;
    double frequency;
    ros::NodeHandle n;
    ros::Publisher pub;
    std::thread jointStateThread;
};

int main(int argc, char **argv) {
    ros::init(argc, argv, "sinusoidal_trajectory", ros::init_options::NoSigintHandler);
    
    // Set the custom Ctrl+C handler
//    signal(SIGINT, SinusoidalTrajectory::sigintHandler);
    signal(SIGINT, monsigintHandler);

    // Instantiate the class
    SinusoidalTrajectory traj;

    // Wait until the program is stopped
    ros::spin();

    return 0;
}
