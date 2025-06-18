#!/usr/bin/env python3
# interact_action.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from typing import Callable, Dict

from stage.actions.action_helper import (
    greet_person,
    react_book,
    react_bottle,
    react_phone,
    react_apple,
    react_glasses,
    react_teddy,
    react_kite,
)

class InteractActionNode(Node):
    def __init__(self) -> None:
        super().__init__('interact_action_node')

        # 1) Mapping commande → fonction
        self._action_map: Dict[str, Callable[[Node], None]] = {
            'greet_person': greet_person,
            'interact:book': react_book,
            'interact:bottle': react_bottle,
            'interact:laptop': react_phone,
            'interact:apple': react_apple,
            'interact:glasses': react_glasses,
            'interact:teddy': react_teddy,
            'interact:kite' :react_kite,
        }

        # 2) Subscription
        self.create_subscription(
            String,
            '/action_command',
            self._on_command,
            10
        )

        self.get_logger().info("✅ InteractActionNode ready, listening on /action_command")

    def _on_command(self, msg: String) -> None:
        """Callback invoked for each /action_command message."""
        cmd: str = msg.data.strip()
        handler = self._action_map.get(cmd)

        if handler:
            handler(self)
            self.get_logger().info(f"✔ Executed action: {cmd}")
        else:
            self.get_logger().warn(f"⚠ Unknown command: {cmd}")

def main(args=None) -> None:
    rclpy.init(args=args)
    node = InteractActionNode()
    try:
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
