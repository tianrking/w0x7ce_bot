from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["0", "0", "0", "0", "0", "0", "base_link", "odom"]
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", "my_robot_rviz_config.rviz"]
        ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            arguments=["my_robot.urdf"],
            output="screen"
        )
    ])

