#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed


class JointStateToNAOqi:
    def __init__(self):
        rospy.init_node("jointstate_to_naoqi", anonymous=True)

        # Publisher : topic attendu par le driver NAOqi
        self.pub = rospy.Publisher(
            "/joint_angles",              # <-- ne change pas
            JointAnglesWithSpeed,
            queue_size=10
        )

        # Subscriber : JointState venant de ROS 2 via le bridge
        rospy.Subscriber(
            "/joint_angles_state",        # <-- topic JointState côté ROS 1
            JointState,
            self.cb_jointstate,
            queue_size=10
        )

        rospy.loginfo(
            "[translator] ✅ prêt : /joint_angles_state (JointState)  →  /joint_angles (JointAnglesWithSpeed)"
        )

    # ----------------------------------------------------------------------
    def cb_jointstate(self, js_msg: JointState):
        """Convertit JointState -> JointAnglesWithSpeed et republie."""
        if not js_msg.name or not js_msg.position:
            # Rien à convertir
            return

        msg = JointAnglesWithSpeed()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ""

        msg.joint_names = list(js_msg.name)
        msg.joint_angles = list(js_msg.position)

        # Choix de la speed : moyenne des vitesses fournies ou 0.2 par défaut
        if js_msg.velocity:
            avg_speed = sum(js_msg.velocity) / float(len(js_msg.velocity))
            msg.speed = max(0.05, min(avg_speed, 1.0))   # clamp 0.05–1.0
        else:
            msg.speed = 0.2

        self.pub.publish(msg)
        rospy.loginfo_once("[translator] Premier JointAnglesWithSpeed publié ✅")
        rospy.logdebug(
            f"[translator] names={msg.joint_names}, angles={msg.joint_angles}, speed={msg.speed:.2f}"
        )


if __name__ == "__main__":
    try:
        JointStateToNAOqi()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
