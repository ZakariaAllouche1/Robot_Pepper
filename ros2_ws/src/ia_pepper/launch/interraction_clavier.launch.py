import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([

        launch_ros.actions.Node(
            package='ia_pepper',
            executable='demande_clavier',
            name='demande_clavier',
            on_exit=launch.actions.Shutdown(),
            output='screen',  # To display output messages in the terminal
            emulate_tty=True,  # To preserve format, color of output messages
        ),

        launch_ros.actions.Node(
            package='ia_pepper',
            executable='mistral_7b_llm',
            name='mistral_7b_llm',
            on_exit=launch.actions.Shutdown(),
            output='screen',  # To display output messages in the terminal
            emulate_tty=True,  # To preserve format, color of output messages
        ),

        launch_ros.actions.Node(
            package='ia_pepper',
            executable='retour_vocal',
            name='retour_vocal',
            on_exit=launch.actions.Shutdown(),
            output='screen',  # To display output messages in the terminal
            emulate_tty=True,  # To preserve format, color of output messages
        ),


        launch_ros.actions.Node(
            package='ia_pepper',
            executable='envoie_commande',
            name='envoie_commande',
            on_exit=launch.actions.Shutdown(),
            output='screen',  # To display output messages in the terminal
            emulate_tty=True,  # To preserve format, color of output messages
        ),



    ])