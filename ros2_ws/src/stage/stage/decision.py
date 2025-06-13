import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class DecisionMakerNode(Node):
    def __init__(self):
        super().__init__('decision_maker_node')
        self.publisher = self.create_publisher(String, '/action_command', 10)
        self.subscription = self.create_subscription(
            String, '/objects_3d', self.decision_callback, 10)
        self.get_logger().info("DecisionMakerNode ready.")

    def decision_callback(self, msg):
        # Attendu : msg.data = '[{"label":"book","x":...}, ...]'
        objects = json.loads(msg.data)
        for obj in objects:
            label = obj.get('label', '')

            # Scénarios simples
            simple_labels = ["book", "bottle", "phone",
                             "apple", "glasses", "teddy"]
            if label in simple_labels:
                self.publisher.publish(String(data=f"interact:{label}"))

            # Scénario salutation (déjà présent chez toi)
            elif label == "person":
                self.publisher.publish(String(data="greet_person"))

            else:
                self.publisher.publish(String(data="unknown_action"))

def main(args=None):
    rclpy.init(args=args)
    node = DecisionMakerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
