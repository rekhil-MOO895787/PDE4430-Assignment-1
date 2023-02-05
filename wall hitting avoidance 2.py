# Import required libraries
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# Define a global variable to track if the turtle is hitting a wall
wall_hit = False

# Define callback function for the turtle's position
def callback(data):
    global wall_hit
    
    linear_speed, angular_speed = vacuum_cleaning(data)
    linear_speed, angular_speed, wall_hit = wall_collision_avoidance(data, linear_speed, angular_speed, wall_hit)
    
    # Publish the twist message
    twist = Twist()
    twist.linear.x = linear_speed
    twist.angular.z = angular_speed
    pub.publish(twist)

def vacuum_cleaning(data):
    linear_speed = 0.0
    angular_speed = 0.0
    
    # Add debug statement to check turtle's x position
    print("Turtle's x position: ", data.x)

    # Check if turtle's x position is less than 5.0
    if data.x <10.0:
        linear_speed = 0.5
        angular_speed = 0.0
        
    return linear_speed, angular_speed

def wall_collision_avoidance(data, linear_speed, angular_speed, wall_hit):
    # Add debug statement to check turtle's x and y positions
    print("Turtle's x position: ", data.x)
    print("Turtle's y position: ", data.y)

    # Check if turtle is close to the edge of the window
    if data.x > 9.5 or data.x < 0.5 or data.y > 9.5 or data.y < 0.5:
        linear_speed = 0.0
        angular_speed = 0.5
        wall_hit = True
    elif wall_hit:
        linear_speed = 0.5
        angular_speed = 0.0
        wall_hit = False
        
    return linear_speed, angular_speed, wall_hit

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('vacuum_cleaner', anonymous=True)

    # Create a publisher object to publish twist messages
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Subscribe to the turtle's position
    rospy.Subscriber('/turtle1/pose', Pose, callback)

    # Keep the node running
    rospy.spin()
