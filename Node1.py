#! /usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def Node1():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rospy.init_node('Node1', anonymous=True)
    rate = rospy.Rate(10)  # 10 hz
    while not rospy.is_shutdown():
        string = "Team Abhiyaan"
        print(string)
        pub.publish(string)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        Node1()
    except rospy.ROSInterruptException:
        pass

    
