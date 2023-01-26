#!/usr/bin/env sh

mkdir -p catkin_ws/src
cd catkin_ws/src

git clone https://github.com/turtlebot/turtlebot_simulator.git
git clone https://github.com/turtlebot/turtlebot.git
git clone https://github.com/turtlebot/turtlebot_apps.git
git clone https://github.com/turtlebot/turtlebot_msgs.git
git clone https://github.com/turtlebot/turtlebot_interactions.git

cd ~/catkin_ws
catkin_make 
