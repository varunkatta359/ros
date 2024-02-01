from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )
    
    turtle_spawner_node = Node(
        package="turtlesim_catch_them_all",
        executable="turtle_spawnnerr",
        parameters=[
            {"spawn_frequency":0.6},
            {"turtle_prefix":"Adarsh_Nibba"}
        ]
    )
    
    turtle_controller_node = Node(
        package="turtlesim_catch_them_all",
        executable="turtlee_controller"
    )
    
    
    
    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld