import rospy
from geometry_msgs.msg import Twist

rospy.init_node('turtle_controller')

turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

twist = Twist()
twist.linear.x = 0.5
twist.angular.z = 0.5

rate = rospy.Rate(10) # 10 Hz
while not rospy.is_shutdown():
    turtle1_pub.publish(twist)
    turtle2_pub.publish(twist)
    rate.sleep()
