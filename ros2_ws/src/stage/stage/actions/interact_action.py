# interact_action.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Actions définies dans action_helper.py
from stage.actions.action_helper import (
    greet_person,
    react_book,
    react_bottle,
    react_phone,
    react_apple,
    react_glasses,
    react_teddy,
)

class InteractActionNode(Node):
    def __init__(self):
        super().__init__("interact_action_node")

        # Publisher /speech (String)
        self._speech_pub = self.create_publisher(String, "/speech", 10)

        # Subscriber /action_command (String)
        self.create_subscription(
            String,
            "/action_command",
            self.cb,
            10,  # QoS profondeur 10
        )

        self.get_logger().info("✅ InteractActionNode prêt (écoute /action_command)")

    # ------------------------------------------------------------------
    def cb(self, msg: String):
        """Route l'action demandée vers la bonne fonction helper."""
        data = msg.data

        if data == "greet_person":
            greet_person(self)
            return

        if data.startswith("interact:"):
            label = data.split(":", 1)[1]
            table = {
                "book": react_book,
                "bottle": react_bottle,
                "laptop": react_phone,
                "apple": react_apple,
                "glasses": react_glasses,
                "teddy": react_teddy,
            }
            action_fn = table.get(label)
            if action_fn:
                action_fn(self)
            else:
                self.get_logger().warn(f'⛔ aucune action définie pour "{label}"')
        else:
            self.get_logger().warn(f'⛔ commande inconnue : "{data}"')


# ----------------------------------------------------------------------
def main(args=None):
    rclpy.init(args=args)
    node = InteractActionNode()
    try:
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
