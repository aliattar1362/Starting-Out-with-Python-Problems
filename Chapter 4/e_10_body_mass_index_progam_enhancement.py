# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 23:11:04 2022

@author: Ali

In programming Exercise #6 in Chapter 3 you were asked to write a program that 
calculates a person’s body mass index (BMI). Recall from that exercise that the BMI is often used
to determine whether a person is overweight or underweight for their height. A person’s
BMI is calculated with the formula
BMI = (weight*703) / (height**2)
where weight is measured in pounds and heightis measured in inches. 
Enhance the program so it displays a message indicating whether the person has optimal weight, is
underweight, or is overweight. A person’s weight is considered to be optimal if his or
her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered
to be underweight. If the BMI value is greater than 25, the person is considered to be
overweight.
"""
# Define the main function.
def main():
    # Ask user to enter his/her weight .
    weight = float(input('Enter your weight (in pounds): '))
    
    # Ask user to enter his/her height .
    height = float(input('Enter your height (in inches): '))
    
    # Call the function (bmi_func) to calculate and displays the BMI index.
    bmi_func(height, weight)
        
# Define the function to calculate and displays the shipping charges.
def bmi_func (height, weight):
    bmi = (weight*703) / (height**2) # The formula to calculate BMI index.
     
    # Define the proper condition based on user's BMI.
    if bmi <= 18.2 and bmi >= 25:
        print('You are in optimal weight!')
    
    elif bmi > 25:
        print('You are in overweight weight!')
    
    else:
        print('You are in underweight weight!')

# Call the main function.    
main()
