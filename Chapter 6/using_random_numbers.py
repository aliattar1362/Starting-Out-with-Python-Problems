# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 00:04:00 2022

@author: Ali

Dr. Kimura teaches an introductory statistics class, and has asked you to write a program
that he can use in class to simulate the rolling of dice.
 The program should randomly generate two numbers in the range of 1 through 6 
 and display them. In your interview with Dr.
Kimura, you learn that he would like to use the program to simulate several rolls of the
dice, one after the other. Here is the pseudocode for the program:
While the user wants to roll the dice:
Display a random number in the range of 1 through 6
Display another random number in the range of 1 through 6
Ask the user if he or she wants to roll the dice again
"""
import random
# This program is generated to simulate the rolling dice. 
# Define the main function.
def main():
    # Define global variable for minimum and maximum random numbers
    MIN = 1
    MAX = 6
    # Initialize the continue the program by entering 'y'
    cont = 'y'

    while cont == 'y' or cont == 'Y':
        first_dice = random.randint(MIN, MAX)
        second_dice = random.randint(MIN, MAX)
        print('The dices pair are: ', first_dice,',', second_dice)
        # Do you want to continue?
        cont = input('Do you want to roll the dice again? (enter \'y\' for yes): ')
           
# Call the main function.    
main()
