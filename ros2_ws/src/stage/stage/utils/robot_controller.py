import rclpy
from std_msgs.msg import String
from sensor_msgs.msg import JointState


# ---------------------------------------------------------------------
def _say(node, text: str):
    """Publie un message sur /speech (publisher créé au besoin)."""
    if not hasattr(node, "_speech_pub") or node._speech_pub is None:
        node._speech_pub = node.create_publisher(String, "/speech", 10)
    node._speech_pub.publish(String(data=text))


# ---------------------------------------------------------------------
def _joint_pub(node):
    """Retourne (ou crée) le publisher JointState vers /joint_angles_state."""
    if not hasattr(node, "_joint_angles_pub") or node._joint_angles_pub is None:
        node._joint_angles_pub = node.create_publisher(
            JointState,
            "/joint_angles_state",   # ← topic intermédiaire
            10,
        )
    return node._joint_angles_pub


# ---------------------------------------------------------------------
def _wave_arm(node):
    """Lève le bras droit (RShoulderPitch = 0.5 rad)."""
    pub = _joint_pub(node)

    js = JointState()
    js.header.stamp = node.get_clock().now().to_msg()
    js.name = [
        "RShoulderPitch",
        "RShoulderRoll",
        "RElbowYaw",
        "RElbowRoll",
        "RWristYaw",
    ]
    js.position = [0.5, 0.0, 0.0, 0.0, 0.0]
    js.velocity = [0.2] * 5
    pub.publish(js)
    node.get_logger().info("▶ /joint_angles_state : wave_arm")


# ---------------------------------------------------------------------
def _shake_head(node):
    """Secoue la tête : droite → gauche → centre."""
    pub = _joint_pub(node)

    # Étape 1 : +0.5 rad
    js1 = JointState()
    js1.header.stamp = node.get_clock().now().to_msg()
    js1.name = ["HeadYaw"]
    js1.position = [0.5]
    js1.velocity = [0.2]
    pub.publish(js1)
    node.get_logger().info("▶ /joint_angles_state : HeadYaw → +0.5")

    # Étape 2 (après 1 s) : –0.5 rad
    def turn_left():
        timer1.cancel()
        js2 = JointState()
        js2.header.stamp = node.get_clock().now().to_msg()
        js2.name = ["HeadYaw"]
        js2.position = [-0.5]
        js2.velocity = [0.2]
        pub.publish(js2)
        node.get_logger().info("▶ /joint_angles_state : HeadYaw → –0.5")

        # Étape 3 (après 1 s) : revenir centre
        def center():
            timer2.cancel()
            js3 = JointState()
            js3.header.stamp = node.get_clock().now().to_msg()
            js3.name = ["HeadYaw"]
            js3.position = [0.0]
            js3.velocity = [0.2]
            pub.publish(js3)
            node.get_logger().info("▶ /joint_angles_state : HeadYaw → 0.0")

        timer2 = node.create_timer(1.0, center)

    timer1 = node.create_timer(1.0, turn_left)


# ---------------------------------------------------------------------
# Actions exposées
def greet_person(node):
    _say(node, "Hello, happy to see you!")
    _wave_arm(node)


def react_book(node):
    _say(node, "Wow, amazing—you are reading books!")
    _shake_head(node)


def react_bottle(node):
    _say(node, "Don't forget to drink water.")
    _shake_head(node)


def react_phone(node):
    _say(node, "You shouldn't waste time on your phone.")
    _shake_head(node)


def react_apple(node):
    _say(node, "Une pomme par jour éloigne le docteur.")
    _shake_head(node)


def react_glasses(node):
    _say(node, "I like your glasses!")
    _shake_head(node)


def react_teddy(node):
    _say(node, "Trop mignonne cette peluche ! Puis-je la câliner ?")
    _shake_head(node)
