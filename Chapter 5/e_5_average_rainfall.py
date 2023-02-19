# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:29:50 2022

@author: Ali

Write a program that uses nested loops to collect data and calculate the average rainfall
 over a period of years. The program should first ask for the number of years. The
outer loop will iterate once for each year. The inner loop will iterate twelve times, 
once for each month. Each iteration of the inner loop will ask the user for the inches
 of rainfall for that month. After all iterations, the program should display the 
 number of months, the total inches of rainfall, and the average rainfall per month 
 for the entire period.
"""
# This program is generated to collect data and calculate the average rainfall
# over a period of years.

# Define the main function.
def main():
    # Define the global variable for numbers of months
    NUM_MON = 12
    total = 0.0
    n = 0
    # ask for the number of years.
    year = int(input('Please enter the number of desired years: '))
    
    for y in range(1, year+1):
        for m in range (NUM_MON):
            # The number of total months of this period
            n += 1
            print('Please enter the amount of rain in month', n, end='')
            rain = float(input(' in inches: '))
            total += rain
    # the average rainfall per month for the entire period.
    ave = total/n
    print('This period consists of', n, 'months in which the total'+ \
          ' amount of rainfall and the average rainfall per month for the entire '+ \
              'period are', total, 'and', ave,'in inches, respectively.')
    
# Call the main function.    
main()