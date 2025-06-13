#!/usr/bin/env python

import rospy
import sys

def print_param(param_name):
    rospy.init_node('print_param')

    # Check if parameter exists
    if rospy.has_param(param_name):
        # Get the parameter value
        param_value = rospy.get_param(param_name)

        # Print the value
        print("Value of parameter '{}': {}".format(param_name, param_value))
    else:
        rospy.logerr("Parameter '{}' does not exist.".format(param_name))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a parameter name.")
    else:
        param_name = sys.argv[1]
        print_param(param_name)
