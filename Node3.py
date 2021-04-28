#! usr/bin/env python
import rospy
from std_msgs.msg import String


def callback1(data):
    print(data.data, end=": ")

def callback2(data):
    print(data.data)
    
def Node3():
    rospy.init_node('Node3', anonymous=True)
    
    rospy.Subscriber('/team_abhiyaan', String, callback1)
    rospy.Subscriber('/autonomy', String, callback2)
    
    rospy.spin()
    
if __name__ == '__main__':
    Node3()
