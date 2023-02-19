# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:55:27 2022

@author: Ali

A painting company has determined that for every 115 square feet of wall space,
 one gallon of paint and eight hours of labor will be required. The company charges $20.00 per
hour for labor. Write a program that asks the user to enter the square feet of wall space to
be painted and the price of the paint per gallon. The program should display the following
data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""

import math

def main():
    # Get the square feet of wall space to be painted
    wall_area = float(input("Enter the square feet of wall space to be painted: "))
    # Get the price of the paint per gallon
    price = float(input("Enter the price of the paint per gallon: "))
    
    estimator_func(wall_area , price)
    
def estimator_func(wall_area , price):
    # For every 115 square feet of wall space, one gallon of paint will be required.
    required_gallon = math.ceil(wall_area /115)
    print("The number of gallons of paint required:", format(required_gallon, ',.0f'))
    # For every 115 square feet of wall space, eight hours of labor will be required. 
    required_hours = required_gallon * 8
    print("The hours of labor required:", format(required_hours, ',.0f'), "h")
    # The cost of the paint
    paint_cost = required_gallon * price
    print("The cost of the paint:", format(paint_cost, ',.0f'), "$")
    # The company charges $20.00 per hour for labor.
    labor_cost = required_hours * 20
    print("The labor charges:", format(labor_cost, ',.0f'), "$")
    # The total cost of the paint job.
    total_cost = paint_cost + labor_cost
    print("The total cost of the paint job is", format(total_cost, ',.0f'), "$")
    
main()
    
    
    
    
    
