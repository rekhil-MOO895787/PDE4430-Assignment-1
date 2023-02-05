import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class TeleopTurtle:
    def __init__(self):
        # initialize node
        rospy.init_node('teleop_turtle')

        # create publisher for turtle velocity
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.speed = 1
        self.movement_bindings = {
            'w': (self.speed, 0),
            'a': (0, self.speed),
            's': (-self.speed, 0),
            'd': (0, -self.speed),
            'x': (0, 0),
        }
        self.speed_bindings = {
            '+': (self.speed + 0.1),
            '-': (self.speed - 0.1),
        }

    def send_velocity(self, linear_x, angular_z):
        # create twist message
        velocity_message = Twist()
        velocity_message.linear.x = linear_x
        velocity_message.linear.y = 0
        velocity_message.linear.z = 0
        velocity_message.angular.x = 0
        velocity_message.angular.y = 0
        velocity_message.angular.z = angular_z

        # publish message
        self.velocity_publisher.publish(velocity_message)

    def change_speed(self, speed):
        self.speed = speed

    def start(self):
        while not rospy.is_shutdown():
            key = input("Enter a movement command: ")
            if key in self.movement_bindings.keys():
                linear_x, angular_z = self.movement_bindings[key]
                self.send_velocity(linear_x, angular_z)
            elif key in self.speed_bindings.keys():
                self.change_speed(self.speed_bindings[key])
                print("Speed changed to: ", self.speed)

if __name__ == '__main__':
    try:
        teleop = TeleopTurtle()
        teleop.start()
    except rospy.ROSInterruptException:
        pass
