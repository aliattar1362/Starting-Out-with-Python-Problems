# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:30:38 2022

@author: Ali

The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.10
Over 2 pounds but not more than 6 pounds $2.20
Over 6 pounds but not more than 10 pounds $3.70
Over 10 pounds $3.80
Write a program that asks the user to enter the weight of a package and then displays the
shipping charges.
"""
# Define the main function.
def main():
    # Ask user to enter the weight of the package.
    weight = float(input('Enter the weight of the package: '))
    
    # Call the function (packages_weight_func) to calculate and displays the shipping charges.
    packages_weight_func(weight)
        
# Define the function to calculate and displays the shipping charges.
def packages_weight_func (num):
     
    # Define the proper condition based on numbers of purchased books.
    if num <= 2:
        rate_per_pound = 1.1 # $1.10 Rate per Pound  
    
    elif num > 2 and num <= 6:
        rate_per_pound = 2.2 # $2.20 Rate per Pound  
        
    elif num > 6 and num <= 10:
        rate_per_pound = 3.7 # $3.70 Rate per Pound  
    
    else:
        rate_per_pound = 3.8 # $3.80 Rate per Pound  
    
    total_price = num * rate_per_pound # The total amount of the purchase after the discount.
    # Display the total amount of the purchase after the discount.
    print('You should pay $', format(total_price, ',.2f'), ' for shipping charges.', sep='')

# Call the main function.    
main()
