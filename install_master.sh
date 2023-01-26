#!/usr/bin/env sh

#creating the work space 
mkdir -p catkin_ws/src
cd catkin_ws/src

# adding the turtlebot function
catkin_create_pkdg human-factors-lab rospy
cd human-factors-lab
mkdir scripts
​
#moving the pilot script to the new repo
mv turtlebot2/pilot.py ~/.catkin_ws/src/humans-factors-lab/scripts
cd ~/catkin_ws
catkin_make 

