# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:16:49 2022

@author: Ali

Write a program that displays a table of the Celsius temperatures 0 through 20 and their
Fahrenheit equivalents. The formula for converting a temperature from Celsius to
Fahrenheit is:
    F=(9/5)C+32
where F is the Fahrenheit temperature and C is the Celsius temperature. Your program
must use a loop to display the table.
"""
# Define the main function.
def main():
    # Define the global variable for final temperature in C. 
    FINAL_TEM = 20
    
    for t in range(FINAL_TEM+1):
        f = (9/5) * t + 32
        print('The temperature is C:', t, 'and F:', format(f, ',.1f')) #Display the salary of each day
        
    
# Call the main function.    
main()
