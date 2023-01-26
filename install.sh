#!/usr/bin/env sh
#creating the work space 
mkdir -p catkin_ws/src
cd catkin_ws/src
# adding the turtlebot function
git clone https://github.com/turtlebot/turtlebot_simulator.git
git clone https://github.com/turtlebot/turtlebot.git
git clone https://github.com/turtlebot/turtlebot_apps.git
git clone https://github.com/turtlebot/turtlebot_msgs.git
git clone https://github.com/turtlebot/turtlebot_interactions.git

cd ~/catkin_ws
catkin_make 
#adding the humans-factors-lab
cd catkin_ws/src
catkin_create_pkdg human-factors-lab rospy

#moving the pilot script to the new repo
mv turtlebot2/pilot.py ~/.catkin_ws/src/humans-factors-lab/

# Copi install.sh in the new repo
mkdir turtlebot2_new
mv turtlebot2/install.sh turtlebot2_new/

# Delete turtlebot2
rm -r turtlebot2

# Rename the new repo
mv turtlebot2_new turtlebot2
