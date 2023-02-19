# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:38:24 2022

@author: Ali

Write a program that calculates the amount of money a person would earn over a period
of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number
of pennies.
"""

# Define the main function.
def main():
    # Ask user to enter the number of days.
    num = int(input('Enter the number of days: '))
    total = 0.0

    for day in range(num+1):
        salary = 2 ** day
        #print(salary, 'for day:', day+1) #Display the salary of each day
        total += salary # In Pensis
    print('The sum of earned salary is:',format(total, ',.0f'), 'Pennis')
    total *= 0.01 # Convert total from Pensis to Dollars
    print('The sum of earned salary is $:',format(total, ',.0f'))
    
# Call the main function.    
main()