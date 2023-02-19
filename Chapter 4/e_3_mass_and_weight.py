# -*- coding: utf-8 -*-
"""
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the
amount of mass of an object in kilograms, you can calculate its weight in newtons with the
following formula:
    
weight = mass * 9.8

Write a program that asks the user to enter an object’s mass, and then calculates its weight.
If the object weighs more than 1,000 newtons, display a message indicating that it is too
heavy. If the object weighs less than 10 newtons, display a message indicating that it is too
light.

"""
# Define the main function.
def main():
    # Get the object’s mass.
    mass = float(input('Enter object’s mass: '))
    
    
    # Call the function (weight_func) to calculate the weight of object.
    weight = weight_func(mass)
    
    
    # Define the proper condition based on object’s weight.
    if weight > 1000 :
        print('It is too heavy.')
    elif weight < 10 :
        print('It is too light.')
    else:
        print('The weight is normal.')

        
    
# Define the function to calculate the weight of object.
def weight_func(mass):
    
    weight = mass * 9.8 # Baed on Newton formula: weight = mass * 9.8
    return(weight)

# Call the main function.    
main()
        
        
        
    
    