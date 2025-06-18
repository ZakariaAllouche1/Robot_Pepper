#!/usr/bin/env python3
import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DecisionMakerNode(Node):
    def __init__(self):
        super().__init__('decision_maker_node')

        # 1) Paramétrage dynamique des labels simples
        self.declare_parameter(
            'simple_labels',
            ['book', 'bottle', 'phone','kite']
        )
        self.simple_labels = (
            self.get_parameter('simple_labels')
                .get_parameter_value()
                .string_array_value
        )

        # 2) Publisher & subscriber
        self.publisher = self.create_publisher(String, '/action_command', 10)
        self.subscription = self.create_subscription(
            String,
            '/objects_3d',
            self.decision_callback,
            10
        )

        self.get_logger().info("✅ DecisionMakerNode ready.")

    def decision_callback(self, msg: String) -> None:
        # 3) Décodage JSON sécurisé
        try:
            objects = json.loads(msg.data)
        except json.JSONDecodeError as e:
            self.get_logger().error(f"JSON invalide sur /objects_3d : {e}")
            return

        # 4) Parcours des objets et publication d’une seule commande
        for obj in objects:
            label = obj.get('label', '')
            if label in self.simple_labels:
                cmd = f"interact:{label}"
            # elif label == 'person':
            #     cmd = "greet_person"
            else:
                cmd = "unknown_action"

            # Publication et log
            self.publisher.publish(String(data=cmd))
            self.get_logger().info(f"→ /action_command : {cmd}")
            return  # on sort dès qu’on a envoyé la première commande


def main(args=None):
    rclpy.init(args=args)
    node = DecisionMakerNode()
    try:
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
