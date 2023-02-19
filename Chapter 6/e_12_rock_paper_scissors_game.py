# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:16:17 2022
@author: Ali

Write a program that lets the user play the game of Rock, Paper, Scissors 
against the computer. The program should work as follows.
1. When the program begins, a random number in the range of 1 through 3 
is generated. If the number is 1, then the computer has chosen rock. 
If the number is 2, then the computer has chosen paper. If the number is 3, 
then the computer has chosen scissors. (Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock”, “paper”, or “scissors” at 
the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
• If one player chooses rock and the other player chooses scissors, 
then rock wins. (The rock smashes the scissors.)
• If one player chooses scissors and the other player chooses paper, 
then scissors wins. (Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then 
paper wins. (Paper wraps rock.)
• If both players make the same choice, the game must be played again to 
determine the winner.
"""
import random
def main():
    coun ='y'
    while coun =='y':
        # Select the number for computer.
        num_1 = random.randrange(1,3)
        # if num_1 == 1, it choosed: rock
        # if num_1 == 2, it choosed: paper
        # if num_1 == 3, it choosed: scissors
        print('Enter 1 for \'rock\'.')
        print('Enter 2 for \'paper\'.')
        print('Enter 3 for \'scissors\'.')
        num_2 = int(input('Enter your number: '))
    
        if num_1 == 1 and num_2 == 3:
            coun ='n'
            print('You lost, and the computer won!')
        elif num_1 == 1 and num_2 == 2:
            coun ='n'
            print('You won, and the computer lost!')
        elif num_1 == 1 and num_2 == 1:
            print('The result is draw! Do the game again!')
        elif num_1 == 2 and num_2 == 3:
            coun ='n'
            print('You lost! The computer won!')
        elif num_1 == 2 and num_2 == 2:
            print('The result is draw! Do the game again!')
        elif num_1 == 2 and num_2 == 1:
            coun ='n'
            print('You won! The computer lost!')
        elif num_1 == 3 and num_2 == 3:
            print('The result is draw! Do the game again!')
        elif num_1 == 3 and num_2 == 2:
            coun ='n'
            print('You won! The computer lost!')
        else:
            coun ='n'
            print('You lost! The computer won!')
main()

