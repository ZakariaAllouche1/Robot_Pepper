import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='morpion',
            executable='object_detection',  
            name='object_detection',
            output='screen',
            parameters=[{'model_path': 'yolov8n.pt'}]  
        ),

        Node(
            package='morpion',
            executable='object_3d_localisation',  
            name='object_3d_localisation',
            output='screen'
        ),
        Node(
            package='morpion',
            executable='board_localization',
            name='board_localization',
            output='screen',
        ),

        Node(
            package='morpion',
            executable='board_state',
            name='board_state',
            output='screen',
        ),
        Node(
            package='morpion',
            executable='morpion_mistral',
            name='morpion_mistral',
            output='screen',
        ),

        Node(
            package='morpion',
            executable='pos_morpion',
            name='pos_morpion',
            output='screen',
        ),
        
        Node(
            package='morpion',
            executable='initialisation',
            name='initialisation',
            output='screen',
        ),
        # Node(
        #     package='morpion',
        #     executable='pepper_head_down',
        #     name='pepper_head_down',
        #     output='screen',
        # ),

    ])
