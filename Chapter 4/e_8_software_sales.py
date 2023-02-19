# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:56:15 2022

@author: Ali

A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity   Discount
10–19       20%
20–49       30%
50–99       40%
100 or more 50%
Write a program that asks the user to enter the number of packages purchased.
The program should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.
"""

# Define the main function.
def main():
    # Ask user to enter the number of packages purchased.
    quantity = int(input('enter the number of packages purchased: '))
    
    # Call the function (packages_func) to displays the amount of the discount (if any) /
    # and the total amount of the purchase after the discount.
    packages_func(quantity)
        
# Define the function to dispaley the amount of the discount (if any) and the total amount of the
# purchase after the discount.
def packages_func (num):
     
    RETAIL_PRICE = 99 # The retail price is $99.
    
    # Define the proper condition based on numbers of purchased books.
    if num < 10:
        discount = 0 # 0% discount.    
    
    elif num >= 10 and num < 19:
        discount = 0.2 # 20% discount
        
    elif num >= 20 and num <= 49:
        discount = 0.3 # 30% discount
        
    elif num >= 50 and num <= 99:
        discount = 0.4 # 40% discount
        
    else:
        discount = 0.5 # 50% discount
    
    total = num * RETAIL_PRICE * (1 - discount) # The total amount of the purchase after the discount.
    # Display the total amount of the purchase after the discount.
    print('You paid $', format(total, ',.2f'), ' to buy the packages.', sep='')

# Call the main function.    
main()