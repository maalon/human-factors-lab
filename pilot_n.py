#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
import csv
import time

# Initializing variables
linear_x = []
angular_z = []
distance_scan = []
angle_scan = []
distance_cmd = []
angle_cmd = []
path = 0
rounds = 0
deriv = []
count = 0
block = 0

def cmd_vel_callback(msg):
    global linear_x, angular_z, distance_cmd, angle_cmd, deriv, path, rounds, count, block
    linear_x.append(msg.linear.x)
    angular_z.append(msg.angular.z)
    distance_cmd.append(msg.linear.x / 1.0) # divide by time
    angle_cmd.append(msg.angular.z)

    # Calculate path
    if len(distance_cmd) > 0 and len(angle_scan) > 0:
        if 0 <= angle_scan[-1] <= 179:
            path += distance_cmd[-1]
        elif 181 <= angle_scan[-1] <= 359:
            path -= distance_cmd[-1]

    # Check if path is 0
    if path == 0:
        count += 1
        if count in [4, 7, 11]:
            rounds = 0
            block += 1
        elif path == 0:
            rounds += 1
            count = 0

    # Reset rounds if block is greater than 3
    if block > 3:
        rounds = 0
        block = 0

    # Calculate derivative
    if len(distance_scan) > 1 and len(linear_x) > 0:
        deriv.append(distance_scan[-1] - distance_scan[-2] - linear_x[-1])

def laser_scan_callback(msg):
    global distance_scan, angle_scan, deriv, path, rounds, count, block
    # Convert laser scan data to numpy array
    laser_data = np.array(msg.ranges)

    # Replace invalid ranges with max range
    laser_data[laser_data == np.inf] = msg.range_max

    # Calculate distance and angle
    angle_scan = np.linspace(msg.angle_min, msg.angle_max, len(laser_data))
    distance_scan = laser_data

    # Calculate path
    if len(distance_cmd) > 0 and len(angle_scan) > 0:
        if 0 <= angle_scan[-1] <= 179:
            path += distance_cmd[-1]
        elif 181 <= angle_scan[-1] <= 359:
            path -= distance_cmd[-1]

def main():
    rospy.init_node('node_name')

    # Subscribing to /cmd_vel topic
    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)

    # Subscribing to /laser_scan topic
    rospy.Subscriber('/laser_scan', LaserScan, laser_scan_callback)

    # Creating CSV file
    filename = "pilot_data_" + str(rospy.get_rostime().to_sec()) + ".csv"
    with open(filename, mode='w') as pilot_data:
        writer = csv.writer(pilot_data)
        writer.writerow(['time', 'linear_x', 'angular_z', 'distance_scan', 'angle_scan', 'distance_cmd', 'angle_cmd', 'path', 'round', 'deriv', 'count', 'block'])

    # Looping at the default rate of 10 Hz
    rate = rospy.Rate(10)

    while not rospy.is_shutdown() and count < 11:
        # Getting current time in hms
        time_str = time.strftime("%H:%M:%S", time.localtime())

        # Writing data to CSV file
        with open(filename, mode='a') as pilot_data:
            writer = csv.writer(pilot_data)
            writer.writerow([time_str, linear_x[-1], angular_z[-1], distance_scan[-1], angle_scan[-1], distance_cmd[-1], angle_cmd[-1], path, round, deriv[-1], count, block])

        rate.sleep()

    rospy.loginfo("Data collection stopped.")
