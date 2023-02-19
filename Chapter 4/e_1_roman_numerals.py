# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message.
"""
# Define the main function.
def main():
    # Get a number between 1-10.
    number = int(input('Enter a number between 1 - 10: '))
    # Call the function to convert the number to its Roman counterpart (peer).
    roman_num_func(number)
    
# Define the function to convert the number to its Roman counterpart (peer).
def roman_num_func(number):
    
    # Define the out of range numbers and correlated error message.
    if number < 1 or number > 10:
        print('Error message: the number is out of range!')
        
    # Define the proper Roman version number for 1-10.
    elif number == 1:
        print('The Roman numeral version of 1 is: I')
    elif number == 2:
        print('The Roman numeral version of 2 is: II')
    elif number == 3:
        print('The Roman numeral version of 3 is: III')
    elif number == 4:
        print('The Roman numeral version of 4 is: IV')
    elif number == 5:
        print('The Roman numeral version of 5 is: V')
    elif number == 6:
        print('The Roman numeral version of 6 is: VI')
    elif number == 7:
        print('The Roman numeral version of 7 is: VII')
    elif number == 8:
        print('The Roman numeral version of 8 is: VIII')
    elif number == 9:
        print('The Roman numeral version of 9 is: IX')
    else:
        print('The Roman numeral version of 10 is: X')

# Call the main function.    
main()
