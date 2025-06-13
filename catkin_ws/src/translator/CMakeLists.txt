cmake_minimum_required(VERSION 3.0.2)
project(translator)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  naoqi_bridge_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/translator_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
