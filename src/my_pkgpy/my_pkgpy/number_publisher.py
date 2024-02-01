import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class Number_Publisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.declare_parameter("number_to_publish", 4)
        self.declare_parameter("number_publishing_frequency", 1.0)
        
        self.number_= self.get_parameter("number_to_publish").value
        self.n_p_f_= self.get_parameter("number_publishing_frequency").value
        
        self.publihser_num=self.create_publisher(Int64,"number_topic",10)
        self.timer_= self.create_timer( 1.0 /self.n_p_f_, self.publish_number)
        self.get_logger().info("this node is started")
        
        
    def publish_number(self):
        msg=Int64()
        msg.data = self.number_
        self.publihser_num.publish(msg)
        
        
        
        
        
         
def main(args=None):
    rclpy.init(args=args)
    node=Number_Publisher()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__=="__main__":
    main()