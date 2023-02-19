# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:59:03 2022

@author: Ali

Write a program that asks the user to enter the amount that he or she has budgeted for a
month. A loop should then prompt the user to enter each of his or her expenses for the
month, and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.
"""
# This program is generated to calculate the distanced traceled. 

# Define the main function.
def main():
    # Initialize the total value of buying expenses
    total = 0.0
    cont = 'y'

    # ask for the user to enter the amount that he or she has budgeted for a month.
    budget = int(input('Please enter the amount that you have budgeted'+\
                      'for a month: '))
    
    while cont == 'y' or cont == 'Y':
        expenses = int(input('Enter your expenses for buying: '))
        total += expenses
        cont = input('Do you want to add next expenses? (enter \'y\' for yes): ')
    if total >= budget:
        print('Your expenses is the over budget. You paid $', format(total, ',.1f'))
    else:
      print('Your expenses is the under budget. You paid $', format(total, ',.1f'))  
        
# Call the main function.    
main()