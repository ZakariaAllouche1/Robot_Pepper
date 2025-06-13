import pygame
import rospy
from geometry_msgs.msg import Twist

# Initialisation de Pygame
pygame.init()

# Initialisation du nœud ROS
rospy.init_node('keyboard_control', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Définir les paramètres de la fenêtre Pygame
window_size = (200, 200)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Commandes directionnelles")

# Variables pour contrôler les mouvements
linear_speed = 0.5
angular_speed = 1.0

def send_cmd_vel(linear, angular):
    """Envoie la commande de déplacement cmd_vel"""
    twist = Twist()
    twist.linear.x = linear
    twist.angular.z = angular
    pub.publish(twist)

# Boucle principale
running = True
while running and not rospy.is_shutdown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gestion des touches appuyées
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                send_cmd_vel(linear_speed, 0)  # Avancer
            elif event.key == pygame.K_DOWN:
                send_cmd_vel(-linear_speed, 0)  # Reculer
            elif event.key == pygame.K_LEFT:
                send_cmd_vel(0, angular_speed)  # Tourner à gauche
            elif event.key == pygame.K_RIGHT:
                send_cmd_vel(0, -angular_speed)  # Tourner à droite
            elif event.key == pygame.K_SPACE:
                send_cmd_vel(0, 0)  # Arrêter le robot

        # Si la touche est relâchée, arrêter le mouvement
        if event.type == pygame.KEYUP:
            send_cmd_vel(0, 0)

# Quitter Pygame
pygame.quit()
