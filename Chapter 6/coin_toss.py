# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 06:48:24 2022

@author: Ali

Using Random Numbers to Represent Other Values
Dr. Kimura was so happy with the dice rolling simulator that you wrote for him, he has
asked you to write one more program. 
He would like a program that he can use to simulate ten coin tosses, 
one after the other. Each time the program simulates a coin toss, it
should randomly display either “Heads” or “Tails”.
You decide that you can simulate the tossing of a coin by randomly generating a number
in the range of 1 through 2. You will write an ifstatement that displays “Heads” if the
random number is 1, or “Tails” otherwise. Here is the pseudocode:
Repeat 10 times:
If a random number in the range of 1 through 2 equals 1 then:
Display ‘Heads’
Else:
Display ‘Tails’
Because the program should simulate 10 tosses of a coin you decide to use a forloop.
"""
import random
# This program is generated to simulate the tossing of a coin. 
# Define the main function.
def main():
    # Define constants for coin tosses, heads and tails.
    HEADS = 1
    TAILS = 2
    TOSSES = 10
    for r in range(TOSSES):
        coin = random.randint(HEADS, TAILS)
        if coin == HEADS:
            print('Heads')
        else:
            print('Tails')

           
# Call the main function.    
main()
