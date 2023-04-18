import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import LaserScan

class RandomLidarPublisher(Node):

    def __init__(self):
        super().__init__('random_lidar_publisher')
        self.publisher_ = self.create_publisher(LaserScan, '/scan', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)  # Publish at 10 Hz
        self.i = 0

    def timer_callback(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'lidar_link'

        num_readings = 360
        range_min = 0.1
        range_max = 10.0

        msg.angle_min = -np.pi
        msg.angle_max = np.pi
        msg.angle_increment = 2 * np.pi / num_readings
        msg.time_increment = 0.0
        msg.scan_time = 0.1
        msg.range_min = range_min
        msg.range_max = range_max

        msg.ranges = np.random.uniform(range_min, range_max, num_readings).tolist()
        msg.intensities = np.random.uniform(0, 100, num_readings).tolist()

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    random_lidar_publisher = RandomLidarPublisher()
    rclpy.spin(random_lidar_publisher)

    random_lidar_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

