import json
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
from std_msgs.msg import Header, String
import rclpy
from rclpy.node import Node
import time 


class DemandeClavier(Node):
    def __init__(self):
        super().__init__('demandeclavier')
        self.publisher_ = self.create_publisher(String, '/relais', 10)

    def bouge_bras(self):
        msg = JointAnglesWithSpeed()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"
        msg.joint_names = ['RShoulderPitch', 'LShoulderPitch']
        msg.joint_angles = [0.5, 0.5]
        msg.speed = 0.1
        msg.relative = False

        # ✅ Transformation en types JSON-compatibles
        msg_dict = {
            "header": {
                "stamp": {
                    "sec": int(msg.header.stamp.sec),
                    "nanosec": int(msg.header.stamp.nanosec)
                },
                "frame_id": str(msg.header.frame_id)
            },
            "joint_names": list(msg.joint_names),
            "joint_angles": list(msg.joint_angles),
            "speed": float(msg.speed),
            "relative": bool(msg.relative)
        }

        # ✅ Conversion en string JSON
        msg_json = json.dumps(msg_dict)

        # Publication via std_msgs/String
        msg_string = String()
        msg_string.data = msg_json
        self.publisher_.publish(msg_string)

        self.get_logger().info('✅ JSON publié sur /relais : ' + msg_json)


def main(args=None):
    rclpy.init(args=args)
    node = DemandeClavier()

    # ✅ Attendre un peu pour laisser ROS démarrer proprement
    node.get_logger().info("🕒 Attente du démarrage complet...")
    time.sleep(2)

    # ✅ Utiliser un timer pour publier après quelques secondes
    node.create_timer(2.0, node.bouge_bras)

    try:
        rclpy.spin(node)  # Laisse tourner le nœud pour gérer les timers/events
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
