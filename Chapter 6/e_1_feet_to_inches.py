# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:16:04 2022

@author: Ali

One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
 of feet as an argument, and returns the number of inches in that many feet. Use the
function in a program that prompts the user to enter a number of feet and then displays
 the number of inches in that many feet.
"""

def main():
    feet = input_func()
    inches = feet_to_inches(feet)
    print('The lenght is', format(inches, ',.0f'), 'inches.')
    
    
def input_func():
    lenght = float(input('Enter a number in feet: '))
    return lenght
           
    
def feet_to_inches(feet):
    inches = feet * 12
    return inches
    
main()