#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from testpython.srv import *

def home_client():
    rospy.wait_for_service('home')
    rospy.wait_for_service('goto')
    
    try:
        home_srv = rospy.ServiceProxy('home', Home)
        resp1 = home_srv()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
    try:
        goto_srv = rospy.ServiceProxy('goto', Goto)
        resp2 = goto_srv(500.0,300.0)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
        return True

if __name__ == "__main__":
    print("Requesting home")
    home_client()
