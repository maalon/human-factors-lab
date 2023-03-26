#!/usr/bin/env sh

#creating the work space 
cd ~
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

# Copi install.sh in the new repo
cd
mkdir turtlebot2_new
mv turtlebot2/install.sh turtlebot2_new/

# Delete turtlebot2
rm -r turtlebot2

# Rename the new repo
mv turtlebot2_new turtlebot2
