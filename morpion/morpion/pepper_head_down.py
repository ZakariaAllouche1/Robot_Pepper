#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class PepperHeadDown(Node):
    def __init__(self):
        super().__init__('pepper_head_down')
        self.pub = self.create_publisher(JointState, '/joint_angles_state', 10)
        self.timer = self.create_timer(1.0, self.move_head_down)
        self.has_moved = False

    def move_head_down(self):
        if self.has_moved:
            return
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = ["HeadPitch"]
        js.position = [0.25]   
        js.velocity = [0.2]
        self.pub.publish(js)
        self.get_logger().info("▶ /joint_angles_state : HeadPitch → 0.25 rad (tête vers le bas)")
        self.has_moved = True  

def main(args=None):
    rclpy.init(args=args)
    node = PepperHeadDown()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
