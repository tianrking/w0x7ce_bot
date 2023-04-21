from flask import Flask, request, jsonify
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.speed_pub = self.create_publisher(Float64, '/speed', 10)
        self.angle_pub = self.create_publisher(Float64, '/angle', 10)

    def send_command(self, speed, angle):
        speed_msg = Float64()
        angle_msg = Float64()

        speed_msg.data = speed
        angle_msg.data = angle

        self.speed_pub.publish(speed_msg)
        self.angle_pub.publish(angle_msg)

controller = None

@app.route('/api/control', methods=['POST'])
def control():
    global controller
    data = request.get_json()
    speed = float(data['speed'])
    angle = float(data['angle'])

    controller.send_command(speed, angle)

    return jsonify(status="success"), 200

if __name__ == '__main__':
    rclpy.init()
    controller = RobotController()
    app.run(host='0.0.0.0', port=5000)
    rclpy.shutdown()

