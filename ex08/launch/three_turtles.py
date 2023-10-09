from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='turtlesim1',
            description='Namespace for turtlesim1'
        ),
        Node(
            package='turtlesim',
            namespace=LaunchConfiguration('namespace'),
            executable='turtlesim_node',
            name='turtle1',
            output='screen',
        ),
        DeclareLaunchArgument(
            'namespace',
            default_value='turtlesim2',
            description='Namespace for turtlesim2'
        ),
        Node(
            package='turtlesim',
            namespace=LaunchConfiguration('namespace'),
            executable='turtlesim_node',
            name='turtle2',
            output='screen',
        ),
        DeclareLaunchArgument(
            'namespace',
            default_value='turtlesim3',
            description='Namespace for turtlesim3'
        ),
        Node(
            package='turtlesim',
            namespace=LaunchConfiguration('namespace'),
            executable='turtlesim_node',
            name='turtle3',
            output='screen',
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic_turtle2',
            namespace='turtlesim2',
            output='screen',
            remappings=[
                ('/input/pose', 'turtle1/pose'),
                ('/output/cmd_vel', 'turtle2/cmd_vel'),
            ],
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic_turtle3',
            namespace='turtlesim3',
            output='screen',
            remappings=[
                ('/input/pose', 'turtle2/pose'),
                ('/output/cmd_vel', 'turtle3/cmd_vel'),
            ],
        ),
    ])
