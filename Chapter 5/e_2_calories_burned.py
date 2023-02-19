# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 02:39:51 2022

@author: Ali

Running on a particular treadmill you burn 3.9 calories per minute. Write a program
that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30
minutes.
"""
# Define the main function.
def main():
    # Define the global varable for the first and last time indicator
    # and the step time (gap time).
    FIRST_TIME = 10
    LAST_TIME = 30
    STEP_TIME = 5
    # Define the global varable for the burned calories per minute
    BURNED_CAL_MIN = 3.9 

    for min in range(FIRST_TIME, LAST_TIME+1, STEP_TIME):
        burn_cal = BURNED_CAL_MIN * min
        print('The total burned calories after', min, ' minutes is:', burn_cal)

# Call the main function.    
main()
