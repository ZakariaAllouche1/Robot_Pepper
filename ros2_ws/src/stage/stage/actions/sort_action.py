import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from stage.utils.robot_controller import sort_ball

class SortActionNode(Node):
    def __init__(self):
        super().__init__('sort_action_node')
        self.subscription = self.create_subscription(
            String,
            '/action_command',  # Topic des commandes d'action
            self.action_callback,
            10
        )

    def action_callback(self, msg):
        if msg.data == "sort_ball":
            sort_ball()  # Appel a une fonction utilitaire pour trier la balle

def main(args=None):
    rclpy.init(args=args)
    node = SortActionNode()
    rclpy.spin(node)
    rclpy.shutdown()
