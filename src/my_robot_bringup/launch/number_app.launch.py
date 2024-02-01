from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    remap_number_topic = ("number_topic","numberrr")
    
    number_pub_node = Node(
        package = "my_pkgpy",
        executable = "number_publish",
        name = "number_publisherrr",
        remappings = [
            remap_number_topic
        ],
        parameters=[
            {"number_to_publish": 9}
        ]
    )
    
    number_counter_node = Node(
        package = "my_pkgpy",
        executable = "number_counter",
        remappings = [
            remap_number_topic,
            ("number_counter_topic","num_counterrr")
        ]
    )
    
    ld.add_action(number_pub_node)
    ld.add_action(number_counter_node)
    return ld