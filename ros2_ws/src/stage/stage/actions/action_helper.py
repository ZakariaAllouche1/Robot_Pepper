#!/usr/bin/env python3
# action_helper.py

"""
Helper functions for Pepper actions.
Each function assumes `node` has:
  - a `/speech` publisher (std_msgs.msg.String) via _get_speech_pub(node)
  - a `/joint_angles_state` publisher (sensor_msgs.msg.JointState) via _get_joint_pub(node)
"""

from std_msgs.msg import String
from sensor_msgs.msg import JointState


def _get_speech_pub(node):
    """Return or create a String publisher on /speech."""
    if not hasattr(node, "_speech_pub") or node._speech_pub is None:
        node._speech_pub = node.create_publisher(String, "/speech", 10)
    return node._speech_pub


def _get_joint_pub(node):
    """Return or create a JointState publisher on /joint_angles_state."""
    if not hasattr(node, "_joint_pub") or node._joint_pub is None:
        node._joint_pub = node.create_publisher(JointState, "/joint_angles_state", 10)
    return node._joint_pub


# def _wave_arm(node):
#     """
#     Wave the right arm: lever le bras puis balancer l'avant-bras 3 fois.
#     """
#     pub = _get_joint_pub(node)

#     def lever_bras():
#         js = JointState()
#         js.header.stamp = node.get_clock().now().to_msg()
#         js.name = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
#         js.position = [0.5, 0.0, 0.0, 1.0, 0.0]  # Le bras est levé, coude plié
#         js.velocity = [0.5] * 5
#         pub.publish(js)
#         node.get_logger().info("Bras droit levé pour wave")
#         # Après 0.6s, commencer le balancement du coude
#         node.create_timer(0.6, lambda: balancer_coude(0))

#     def balancer_coude(i):
#         # Balancement de l'avant-bras (RElbowRoll)
#         js = JointState()
#         js.header.stamp = node.get_clock().now().to_msg()
#         js.name = ["RElbowRoll"]
#         # Alterne entre 1.0 et 0.3 radians
#         js.position = [1.0 if i % 2 == 0 else 0.3]
#         js.velocity = [0.5]
#         pub.publish(js)
#         if i < 5:
#             node.create_timer(0.4, lambda: balancer_coude(i+1))
#         else:
#             # Rendre le bras à la position neutre
#             node.create_timer(0.6, reposer_bras)

#     def reposer_bras():
#         js = JointState()
#         js.header.stamp = node.get_clock().now().to_msg()
#         js.name = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
#         js.position = [1.5, 0.0, 0.0, 0.0, 0.0]  # position neutre
#         js.velocity = [0.5] * 5
#         pub.publish(js)
#         node.get_logger().info("Bras reposé")

#     # Démarre la séquence
#     lever_bras()



def _shake_head(node):
    """Shake head: right (+0.5), left (-0.5), then center (0) at 1s intervals."""
    pub = _get_joint_pub(node)

    def step1():
        js1 = JointState()
        js1.header.stamp = node.get_clock().now().to_msg()
        js1.name = ["HeadYaw"]
        js1.position = [0.5]
        js1.velocity = [0.2]
        pub.publish(js1)
        node.get_logger().info("▶ /joint_angles_state: HeadYaw → +0.5")
        node.create_timer(1.0, step2)

    def step2():
        js2 = JointState()
        js2.header.stamp = node.get_clock().now().to_msg()
        js2.name = ["HeadYaw"]
        js2.position = [-0.5]
        js2.velocity = [0.2]
        pub.publish(js2)
        node.get_logger().info("▶ /joint_angles_state: HeadYaw → -0.5")
        node.create_timer(1.0, step3)

    def step3():
        js3 = JointState()
        js3.header.stamp = node.get_clock().now().to_msg()
        js3.name = ["HeadYaw"]
        js3.position = [0.0]
        js3.velocity = [0.2]
        pub.publish(js3)
        node.get_logger().info("▶ /joint_angles_state: HeadYaw → 0.0")

    # kick off the sequence
    step1()


def _say(node, text: str):
    """Publish a text string to /speech."""
    pub = _get_speech_pub(node)
    pub.publish(String(data=text))
    node.get_logger().info(f"▶ /speech: {text}")


# Exposed actions

def greet_person(node):
    """Greet: say hello and wave arm."""
    _say(node, "Hello, happy to see you!")
    _wave_arm(node)


def react_book(node):
    """React to a book: comment and shake head."""
    _say(node, "Wow, amazing—you are reading books!")
    _shake_head(node)


def react_bottle(node):
    """React to a bottle: reminder to drink."""
    _say(node, "Don't forget to drink water.")
    _wave_arm(node)


def react_phone(node):
    """React to a laptop/phone: compliment usage."""
    _say(node, "You know how to use a laptop nice.")
    _shake_head(node)


def react_apple(node):
    """React to an apple: proverb."""
    _say(node, "Une pomme par jour éloigne le docteur.")
    _shake_head(node)


def react_glasses(node):
    """React to glasses: compliment."""
    _say(node, "I like your glasses!")
    _shake_head(node)


def react_teddy(node):
    """React to a teddy: ask to cuddle."""
    _say(node, "Trop mignonne cette peluche ! Puis-je la câliner ?")
    _shake_head(node)


def react_kite(node):
    "react to a kite"
    _say(node, "let's play")
    _wave_arm(node)