#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts


class Addstwointegersclientnode(Node):

    def __init__(self):
        super().__init__("Adds_two_Integers_client")
        self.call_add_two_ints_server(6,4)
    
    
    def call_add_two_ints_server(self,a,b):
          client = self.create_client(AddTwoInts,"adds_two_integers")
          while not client.wait_for_service(1.0):
              self.get_logger().warn("waiting for the server Add_Two_Integers ..") 
              
          request = AddTwoInts.Request()
          request.a = a
          request.b = b
    
          future = client.call_async(request)
          future.add_done_callback(partial(self.callback_call_addtwoints,a=a,b=b))
          
    def callback_call_addtwoints(self,future,a,b):
          try :
              response = future.result()
              self.get_logger().info(f"{str(a)} + {str(b)} = {str(response.sum)} ")
          except Exception as e :
              self.get_logger().error("service call failed %r"%(e,))
    
 
def main(args=None):
    rclpy.init(args=args)
    node = Addstwointegersclientnode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()