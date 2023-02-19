# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:47:40 2022

@author: Ali

A bug collector collects bugs every day for seven days.
Write a program that keeps a running total of the number of bugs collected during the seven days.
The loop should ask for the number of bugs collected for each day,
and when the loop is finished, the program
should display the total number of bugs collected.
"""

# Define the main function.
def main():
    # Define the global varable for the length of desired period
    # Here the desire period is 7 days (days of a week)
    TOTAL_DAYS = 7
    # Initialize the total number of bugs before staring the work.
    total_bug = 0
    # Ask user to enter number of bugs collected for each day in a for loop.
    for day in range(TOTAL_DAYS):
        # Get the number of bugs for each day.
        print('Enter the number of bugs you collected in day' , day+1,end='') 
        num_bug = int(input(' : '))
        # Add the number of collected bugs for each day to toal number of bugs.
        total_bug += num_bug
    print('The total collected bugs in this week is:', total_bug)

# Call the main function.    
main()
