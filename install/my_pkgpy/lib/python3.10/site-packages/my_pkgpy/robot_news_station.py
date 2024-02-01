#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class RobotNewsStation(Node): 
    def __init__(self):
        super().__init__("robot_news_stationnn")
        self.declare_parameter("robot_name", "default")

        self.robot_name = self.get_parameter("robot_name").value
        
        self.publisher_ = self.create_publisher(String,"robot_news" ,10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("The Robot News Station is Started")

    def publish_news(self):
        msg = String()
        msg.data = ("Hi, This is {}".format(str(self.robot_name)))
        # Publish the message to the topic 'robot_news'
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()