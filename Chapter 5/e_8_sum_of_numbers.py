# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:28:45 2022

@author: Ali

Write a program with a loop that asks the user to enter a series of positive numbers. The
user should enter a negative number to signal the end of the series. After all the positive
numbers have been entered, the program should display their sum.
"""

# Define the main function.
def main():
    # Ask user to enter the number of rows.
    num = int(input('Enter the number: '))
    total = 0.0

    while num >= 0:
        total += num
        print('Enter negative point if you want to be quit form this program!')
        num = int(input('Enter the next number: '))
    print('The sum of all entered numbers are:',format(total, ',.0f'))
    
# Call the main function.    
main()