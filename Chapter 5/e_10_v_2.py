# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 02:47:25 2022

@author: Ali

Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""

# Define the main function.
def main():
    # Ask user to enter the number of rows.
    rows = int(input('Enter the number of rows: '))
    # Ask user to enter the number of columns.
    cols = int(input('Enter the number of columns: '))

    for r in range(rows):
        print('#', end='')
        for c in range(cols):
            if r != c:
                print(' ', end='')
            else: 
                print('#')
                break
# Call the main function.    
main()
