# Import necessary packages
import rospy
import sys
import time
from turtlesim.srv import Spawn, SpawnRequest, TeleportAbsolute

# Create the node and set up the service clients
rospy.init_node("turtlesim_controller")
spawn_turtle = rospy.ServiceProxy("spawn", Spawn)
teleport_turtle = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)

# Set up the position of the second turtle
position = [2.0, 2.0, 0.0]

# Spawn the first turtle
first_turtle = spawn_turtle(x=position[0], y=position[1], theta=position[2])

# Set up the position of the third turtle
position = [8.0, 8.0, 0.0]

# Spawn the second turtle
second_turtle = spawn_turtle(x=position[0], y=position[1], theta=position[2])

# Set up the position of the fourth turtle
position = [4.0, 6.0, 0.0]

# Spawn the third turtle
third_turtle = spawn_turtle(x=position[0], y=position[1], theta=position[2])

# Teleport the second turtle to a new position
teleport_turtle(x=8.0, y=8.0, theta=0.0)

# Wait for a while before finishing the node
time.sleep(2)