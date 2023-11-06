from rclpy.node import Node


class Controller(Node):
    def __init__(self, name):
        super().__init__(name)