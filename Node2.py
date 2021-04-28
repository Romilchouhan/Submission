#! /usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def Node2():
    pub = rospy.Publisher('/autonomy', String, queue_size=10)
    rospy.init_node('Node2', anonymous=True)
    rate = rospy.Rate(10)  # 10 hz
    while not rospy.is_shutdown():
        string = "Fueled By Autonomy"
        print(string)
        pub.publish(string)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        Node2()
    except rospy.ROSInterruptException:
        pass

    
