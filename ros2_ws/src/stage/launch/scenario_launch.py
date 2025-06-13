# import launch
# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     return LaunchDescription([
        
#         Node(
#             package='stage',
#             executable='object_detection',  
#             name='object_detection_node',
#             output='screen',
#             parameters=[{'model_path': 'yolov8n.pt'}]  
#         ),

#         Node(
#             package='stage',
#             executable='decision',  
#             name='decision_node',
#             output='screen'
#         ),

#         # Node(
#         #     package='stage',
#         #     executable='greet_action',  
#         #     name='greet_action_node',
#         #     output='screen'
#         # ),

#         #Node(
#         #    package='stage',
#         #    executable='sort_action',  
#         #    name='sort_action_node',
#         #    output='screen'
#         #),

#         Node(
#             package='stage',
#             executable='object_3d_localisation',  
#             name='object_3d_localisation_node',
#             output='screen'
#         ),


#         Node(                         
#             package='stage',
#             executable='interact_action',
#             name='interact_action_node',
#             output='screen'
#         ),
#     ])



import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    share_dir = get_package_share_directory('stage')
    model_dir = os.path.join(share_dir, 'yolov8n_ncnn_model')

    param_file = os.path.join(model_dir, 'yolov8n_fp16.param')
    bin_file   = os.path.join(model_dir, 'yolov8n_fp16.bin')

    return LaunchDescription([
        Node(
            package='stage',
            executable='object_detection',
            name='object_detection_node',
            output='screen',
            parameters=[
                {'param_file': param_file},
                {'bin_file':   bin_file},
            ],
        ),
        Node(
            package='stage',
            executable='decision',
            name='decision_node',
            output='screen',
        ),
        Node(
            package='stage',
            executable='object_3d_localisation',
            name='object_3d_localisation_node',
            output='screen',
        ),
        Node(
            package='stage',
            executable='interact_action',
            name='interact_action_node',
            output='screen',
        ),
    ])
