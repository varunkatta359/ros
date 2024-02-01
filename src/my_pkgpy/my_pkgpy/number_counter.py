#!usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class numbercounterNode(Node):
    def __init__(self):
        super().__init__("number_counter_node")
        self.counter=0
        self.number_counter_=self.create_subscription(Int64,"number_topic",self.callback_number_topic,10)
        self.number_counter_publisher=self.create_publisher(Int64,"number_counter_topic",10)
        self.reset_counter_service=self.create_service(SetBool,"reset_counter",self.callback_reset_counter)
        self.get_logger().info("node crazy started")
        
        
    def callback_number_topic(self,msg):
        self.counter += msg.data
        message = Int64()
        message.data = self.counter
        self.number_counter_publisher.publish(message)  
        
    def callback_reset_counter(self,request,response):
        if request.data:
            self.counter=0
            response.success = True
            response.message="counter is reset"
        else:
            response.success = False
            response.message="counter is not reset"
        return response 
            
            
            
            
def main(args=None):
    rclpy.init(args=args)
    node=numbercounterNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
            