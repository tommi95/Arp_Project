#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32
import random
import time

goal = PoseStamped()


def callback(msg, args):
    ex = msg.pose.pose.position.x - goal.pose.position.x
    ey = msg.pose.pose.position.y - goal.pose.position.y
    pub = args[0]
    pub2 = args[1]

    if((ex*ex + ey*ey) < 0.1):
        pub2.publish(ex*ex + ey*ey)

        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x = random.randrange(-5, 5)
        goal.pose.position.y = random.randrange(-5, 5)
        goal.pose.position.z = 0
        goal.pose.orientation.x = 0
        goal.pose.orientation.y = 0
        goal.pose.orientation.z = 0
        goal.pose.orientation.w = 1
        pub.publish(goal)



def coord():
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    pub2 = rospy.Publisher('/debug', Float32, queue_size=10)

    rospy.init_node('coordinator', anonymous=True)
    rate = rospy.Rate(10)

    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = 4.0
    goal.pose.position.y = -4.0
    goal.pose.position.z = 0

    goal.pose.orientation.x = 0
    goal.pose.orientation.y = 0
    goal.pose.orientation.z = 0
    goal.pose.orientation.w = 1
    time.sleep(15)
    first_round = 1

    while not rospy.is_shutdown():
        if(first_round == 1):
            pub.publish(goal)
            first_round = 0
        rospy.Subscriber("/odometry/filtered", Odometry, callback,(pub, pub2))
        rate.sleep()

if __name__ == '__main__':
    try:
        coord()
    except rospy.ROSInterruptException:
        pass
