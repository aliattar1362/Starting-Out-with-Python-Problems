# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 08:20:54 2022

@author: Ali
Write a program that generates a random number in the range of 1 through 100 and asks the
user to guess what the number is. If the user’s guess is higher than the random number, 
the program should display “Too high, try again.” If the user’s guess is lower than the random
 number, the program should display “Too low, try again.” If the user guesses the number, 
 the application should congratulate the user and then generate a new random number 
 so the game can start over.
Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
user makes. When the user correctly guesses the random number, the program should display
the number of guesses.
"""
import random
def main():
    # Boolean vairable to continue the program 
    coun_pro = True
    while coun_pro == True:
        answer = False
        actual_number = random.randrange(1, 100)
        while answer != True:
            my_number = input_func()
            if my_number > actual_number:
                print('Too high, try again.')
            elif my_number < actual_number:
                print('Too low, try again.')
            else:
                print('Congratulation! You gussed the right number!')
                answer = True
                print('answer:', answer)
                coun = input('Do you want to continue the game? Enter \'y\' or \'Y\' as yes!: ')
                
        if coun == 'y' or coun == 'Y':
            coun_pro = True
        else: 
            coun_pro = False

def input_func():
    guess = int(input('Enter your guess about the number: '))
    return guess

main()