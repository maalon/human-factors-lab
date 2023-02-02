#!/usr/bin/env python
import rospy
import csv
import time
import numpy as np
import pandas as pd
import serial

# Global variable to keep track of the number of times the experience is done
experience_count = 0
count = 0
# ser = serial.Serial('COM3', 9600) # specify the correct serial port and baud rate for your Arduino

# Create a list to store the distance values
distances = []
x = []
def follower_callback(data):
    global experience_count
    arduino_data = ser.readline().decode().strip() # read the data from the Arduino
    # extract the necessary information from the odometry message
    x = data.pose.pose.position.x
    # add the x of the robot
    x = x.append(x)
    # y = data.pose.pose.position.y
    # extract the distance from the person
    distance = data.pose.pose.position.z
    # add the distance to the list
    distances.append(distance)
    # calculate the variance of the distances
    distance_variance = np.var(distances)
    # calculate the difference between the distance and the wanted distance
    distance_diff = distance - 0.6
    # get the current date
    current_date = time.strftime("%Y-%m-%d", time.gmtime())
    # get the current time
    current_time = time.strftime("%H:%M:%S", time.gmtime())
    # create the file name
    file_name = 'pilot_data_{}_{}_{}.csv'.format(current_date,current_time, experience_count)
    # write the data to a CSV file
    with open(file_name, mode='a') as csv_file:
        fieldnames = ['Time', 'X', 'Distance', 'Distance Diff', 'r-speed', 'h-speed']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Time': current_time, 'X': x, 'Distance': distance, 'Distance Diff': distance_diff, 'r-speed': ,'h-speed': })
    print("Data written to CSV file")
