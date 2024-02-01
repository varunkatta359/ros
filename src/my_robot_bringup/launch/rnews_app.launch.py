from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    
    robot_names = ["pAlLaVi","SruThI","ThuLaSi"]
    robot_news_station_nodes = []
    
    for names in robot_names:
        robot_news_station_nodes.append(Node(
            package="my_pkgpy",
            executable="robot_news_station",
            name="robot_news_station"+ names.lower(),
            parameters=[
                {"robot_name":names[0].upper()+names[1::].lower()}
            ]
            
        ) )
    
    
    smartphone_node = Node(
        package="my_pkgpy",
        executable="smartphone"
    )
    
    for node in robot_news_station_nodes:
        ld.add_action(node)
    ld.add_action(smartphone_node)
    return ld