# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:29:48 2022

@author: Ali

The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
The program should then determine whether the month times the day equals the year.
 If so, it should display a message saying the date is magic.
Otherwise, it should display a message saying the date is not magic.

"""
# Define the main function.
def main():
    # Get the user's date.
    # First ask the month (in numeric form).
    month = int(input('Enter desire month: '))
    # Second ask the day (in numeric form).
    day = int(input('Enter desire day: '))
    # First ask the two-digit year (in numeric form).
    year = int(input('Enter desire year in two-digit format: '))
    
    
    # Call the function (date_magic_func) to determine whether the month times the day equals the year.
    date_magic_func(month, day, year)
        
# Define the function to to determine whether the month times the day equals the year.
def date_magic_func(month, day, year):
     
    # Define the proper condition based on object’s weight.
    # Find first digit of day
    day_first_digit = day % 10
    if month <= 9 and  year == (day_first_digit+(month*10)):
        print('The date is magic.')
    else:
        print('The date is not magic.')


# Call the main function.    
main()
        
        
        
    

