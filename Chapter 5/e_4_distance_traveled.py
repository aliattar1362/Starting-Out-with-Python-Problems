# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:52:22 2022

@author: Ali

The distance a vehicle travels can be calculated as follows:
distance = speed * time
For example, if a train travels 40 miles per hour for three hours, the distance traveled
 is 120 miles. Write a program that asks the user for the speed of a vehicle
 (in miles per hour) and the number of hours it has traveled. 
 It should then use a loop to display the distance the
vehicle has traveled for each hour of that time period. Here is an example of the desired
output:
What is the speed of the vehicle in mph? 40 Enter
How many hours has it traveled? 3 Enter
Hour        Distance Traveled
-----------------------------
1           40 
2           80 
3           120
"""

# This program is generated to calculate the distanced traceled. 

# Define the main function.
def main():
    # Initilize the passed time
    distance = 0
    # ask for the speed of a vehicle (in miles per hour)
    # and the number of hours it has traveled. 
    speed = int(input('Please enter the speed of a vehicle (in miles per hour): '))
    duration = int(input('Please enter the number of hours you have traveled: '))
    print('Hour\tDistance Traveled')
    print('-------------------------')
    
    for y in range(1, duration+1):
            distance += speed
            print(y, 2*'\t', distance)

# Call the main function.    
main()