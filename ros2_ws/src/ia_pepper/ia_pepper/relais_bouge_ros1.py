from  naoqi_bridge_msgs.msg import JointAnglesWithSpeed
from std_msgs.msg import Header
import rclpy
from rclpy.node import Node


class DemandeClavier(Node):
    def __init__(self):
        super().__init__('demandeclavier')
        
        self.suscription = self.create_subscription(JointAnglesWithSpeed,'/relais',callback,10)
        self.suscription 

        self.publisher_ = self.create_publisher(JointAnglesWithSpeed, '/relais_ros1', 10)
        self.message = JointAnglesWithSpeed()

    def callback(self, msg):
        self.message = message


def main(args=None):
    rclpy.init(args=args)
    node = DemandeClavier()
    node.bouge_bras()

    # Laisse tourner quelques secondes puis termine
    rclpy.spin_once(node, timeout_sec=2.0)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()