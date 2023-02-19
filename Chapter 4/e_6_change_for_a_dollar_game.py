# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 00:32:29 2022

@author: Ali

Create a change-counting game that gets the user to enter the number of coins required to make
exactly one dollar. The program should prompt the user to enter the number of pennies, 
nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, 
the program should congratulate the user for winning the game. 
Otherwise, the program should display a message indicating whether the amount 
entered was more than or less than one dollar.
"""
# Define the main function.
def main():
    # Ask user to enter the number of coins required to make exactly one dollar.
    print('Enter the number of coins required to make exactly one dollar:')
    pennies = int(input('Enter the number of pennies: '))
    nickels = int(input('Enter the number of nickels: '))
    dimes = int(input('Enter the number of dimes: '))
    quarters = int(input('Enter the number of quarters: '))
    
    # Call the function (dollar_game_func) to determine the user win the game or not.
    dollar_game_func(pennies, nickels, dimes, quarters)
        
# Define the function to to determine the user win the game or not.
def dollar_game_func (pennies, nickels, dimes, quarters):
    # Convert the coins to their dollars correlated
    pennies = pennies * 0.01 # 1 pennis = 0.01$
    nickels = nickels * 0.05 # 1 pennis = 0.05$
    dimes = dimes * 0.1 # 1 pennis = 0.1$
    quarters = quarters * 0.25 # 1 pennis = 0.25$
    
    # Calculate the total amount of coins
    total = pennies + nickels + dimes + quarters
    
    # Define the proper condition based input colors.
    if total == 1:
        print('Congratulation! You won the game!')
        
    else: 
        print('The amount entered was more than or less than one dollar.')

# Call the main function.    
main()
        
        
        
    

