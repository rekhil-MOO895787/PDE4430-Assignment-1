#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def robot1_callback(data):
    # Get the current position of robot 1
    x = data.x
    y = data.y

    # Define the avoidance condition for robot 1
    if x > 10 and y > 10:
        # Publish the twist message to move robot 1 away from the object
        twist = Twist()
        twist.linear.x = -0.7
        twist.angular.z = 0.5
        pub1.publish(twist)
    else:
        # Publish the twist message to move robot 1 towards the object
        twist = Twist()
        twist.linear.x = 0.7
        twist.angular.z = -0.5
        pub1.publish(twist)

def robot2_callback(data):
    # Get the current position of robot 2
    x = data.x
    y = data.y

    # Define the avoidance condition for robot 2
    if x > 10 and y < 10:
        # Publish the twist message to move robot 2 away from the object
        twist = Twist()
        twist.linear.x = -0.7
        twist.angular.z = -0.5
        pub2.publish(twist)
    else:
        # Publish the twist message to move robot 2 towards the object
        twist = Twist()
        twist.linear.x = 0.8
        twist.angular.z = 0.5
        pub2.publish(twist)
def robot3_callback(data):
    # Get the current position of robot 1
    x = data.x
    y = data.y

    # Define the avoidance condition for robot 1
    if x > 10 and y > 10:
        # Publish the twist message to move robot 1 away from the object
        twist = Twist()
        twist.linear.x = -0.7
        twist.angular.z = 1.5
        pub3.publish(twist)
    else:
        # Publish the twist message to move robot 1 towards the object
        twist = Twist()
        twist.linear.x = 0.7
        twist.angular.z = -0.5
        pub3.publish(twist)
def robot4_callback(data):
    # Get the current position of robot 1
    x = data.x
    y = data.y

    # Define the avoidance condition for robot 1
    if x > 10 and y > 10:
        # Publish the twist message to move robot 1 away from the object
        twist = Twist()
        twist.linear.x = -2.7
        twist.angular.z = 0.5
        pub4.publish(twist)
    else:
        # Publish the twist message to move robot 1 towards the object
        twist = Twist()
        twist.linear.x = 0.7
        twist.angular.z = -0.5
        pub4.publish(twist)
if __name__ == '__main__':
    rospy.init_node('multiple_robot_controller')

    # Subscribe to the pose topic for robot 1
    sub1 = rospy.Subscriber('/turtle1/pose', Pose, robot1_callback)

    # Subscribe to the pose topic for robot 2
    sub2 = rospy.Subscriber('/turtle2/pose', Pose, robot2_callback)

    # Publish to the twist topic for robot 1
    pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Publish to the twist topic for robot 2
    pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

     # Subscribe to the pose topic for robot 3
    sub3 = rospy.Subscriber('/turtle3/pose', Pose, robot3_callback)

    # Subscribe to the pose topic for robot 4
    sub4 = rospy.Subscriber('/turtle4/pose', Pose, robot4_callback)

    # Publish to the twist topic for robot 3
    pub3 = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10)

    # Publish to the twist topic for robot 4
    pub4 = rospy.Publisher('/turtle4/cmd_vel', Twist, queue_size=10)


    rospy.spin()
