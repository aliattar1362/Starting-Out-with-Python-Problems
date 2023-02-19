# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:12:37 2022

@author: Ali

Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*
"""

# Define the main function.
def main():
    # Ask user to enter the number of rows.
    rows = int(input('Enter the number of rows and columns: '))
    # Ask user to enter the number of columns.
    #cols = int(input('Enter the number of columns: '))

    for r in range(rows,0,-1):
        #print('*', end='')
        for c in range(r):
            print('#', end='')
        print()
# Call the main function.    
main()