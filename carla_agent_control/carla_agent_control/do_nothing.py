import rclpy
from .controllers import Controller


class DoNothingNode(Controller):
    def __init__(self):
        super().__init__(name='do_nothing_controller')
        self.get_logger().info('Doing nothing!')


def main(args=None):
    rclpy.init(args=args)

    controller = DoNothingNode()

    rclpy.spin(controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    controller.destroy_node()
    rclpy.shutdown()
