# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:22:40 2022

@author: Ali

Write a function named maximum that accepts two integer values as arguments and returns
the value that is the greater of the two. For example, if 7 and 12 are passed as arguments
to the function, the function should return 12. Use the function in a program that prompts
the user to enter two integer values. The program should display the value that is the
greater of the two.
"""
def main():
    n_1, n_2 = input_func()
    g = maximum_func(n_1, n_2)
    display_func(g)
    
    
def input_func():
    # Get the two desired numbers.
    n_1 = int(input('Enter the first number: '))
    n_2 = int(input('Enter the second number: '))
    return n_1, n_2

def display_func(num):
    print('Between these two numbers,', num, 'is greather.')

def maximum_func(num1, num2):
    # Initialize the greater number
    g = 0
    if num1 > num2:
        g = num1
    else:
        g = num2
        
    return g
    
main()
    