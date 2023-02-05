#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def main():
    rospy.init_node('my_node_name', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
def move(speed, distance, is_forward):
    velocity_message = Twist()
    if is_forward:
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0

    distance_moved = 0.0
    loop_rate = rospy.Rate(10) # 10hz
    while distance_moved < distance:
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        distance_moved = distance_moved + abs(speed) * (1.0/10.0)

def rotate(angular_speed, relative_angle, clockwise):
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0

    if clockwise:
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # 10hz
    while angle_moved < relative_angle:
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        angle_moved = angle_moved + abs(angular_speed) * (1.0/10.0)

current_angle_degrees = 0
def set_desired_orientation(desired_angle_degrees):
    relative_angle = desired_angle_degrees - current_angle_degrees
    if relative_angle < 0:
        rotate(math.radians(10), abs(relative_angle), False)
    else:
        rotate(math.radians(10), abs(relative_angle), True)

def vacuum_cleaning():
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # Move to bottom left corner
    move(1.0, 9.0, True)
    set_desired_orientation(270) # face down

    # Move along bottom wall
    move(1.0, 11.0, True)
    set_desired_orientation(0) # face right

    # Move along right wall
    move(1.0, 9.0, True)
    set_desired_orientation(90) # face up

    # Move along top wall
    move(1.0, 11.0, True)
    set_desired_orientation(180) # face left

    # Move along left wall
    move(1.0, 9.0, True)
    set_desired_orientation(270) # face down
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

if __name__ == '__main__':

    try:
        main()
        vacuum_cleaning()
    except rospy.ROSInterruptException:
        pass

