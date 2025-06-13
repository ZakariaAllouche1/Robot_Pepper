cmake_minimum_required(VERSION 2.8.3)
project(joint_state_publisher_cpp)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(joint_state_publisher src/joint_state_publisher.cpp)
target_link_libraries(joint_state_publisher ${catkin_LIBRARIES})

add_executable(joint_state_publisher_cpp src/joint_state_publisher_cpp.cpp)
target_link_libraries(joint_state_publisher_cpp ${catkin_LIBRARIES})

add_executable(joint2vect3 src/joint2vect3.cpp)
target_link_libraries(joint2vect3 ${catkin_LIBRARIES})

add_executable(joint_state_publisher_cpp_thread src/joint_state_publisher_cpp_thread.cpp)
target_link_libraries(joint_state_publisher_cpp_thread ${catkin_LIBRARIES})

# Ajoutez ces lignes pour prendre en charge le thread
find_package(Threads REQUIRED)
target_link_libraries(joint_state_publisher_cpp_thread ${CMAKE_THREAD_LIBS_INIT})
