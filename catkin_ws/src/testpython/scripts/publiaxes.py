import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

if __name__ == '__main__':
    # Initialiser le nœud ROS
    rospy.init_node('axes_repere_rviz_publisher')

    # Créer un éditeur de messages pour publier la pose des axes
    axes_pub = rospy.Publisher('axes_repere', PoseStamped, queue_size=10)

    # Fréquence de publication
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Créer un message PoseStamped pour les axes du repère
        pose_msg = PoseStamped()

        # Remplir les informations de position
        pose_msg.pose.position.x = 0.0
        pose_msg.pose.position.y = 0.0
        pose_msg.pose.position.z = 0.0

        # Remplir les informations d'orientation (par défaut, axes alignés avec le repère global)
        pose_msg.pose.orientation.x = 0.0
        pose_msg.pose.orientation.y = 0.0
        pose_msg.pose.orientation.z = 0.0
        pose_msg.pose.orientation.w = 1.0

        # Publier le message de pose des axes
        axes_pub.publish(pose_msg)

        # Attendre jusqu'à la prochaine itération de la boucle
        rate.sleep()
