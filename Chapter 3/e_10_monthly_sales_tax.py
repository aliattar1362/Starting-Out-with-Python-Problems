# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:27:19 2022

@author: Ali

A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 4 percent
and the county sales tax rate is 2 percent. Write a program that asks the user to enter the
total sales for the month. From this figure, the application should calculate and display the
following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)

"""

def main():
    # Get the total sales for the month.
    total_sales = float(input("Please enter the total sales for the month: "))
    sales_tax_func(total_sales)

    
def sales_tax_func(total_sales):
    # The county sales tax is 2 percent
    county_tax = total_sales * 0.02
    # Display county sales tax
    print("The county sales tax was", format(county_tax, ',.0f'), "$")
    
    # The state sales tax is 4 percent
    state_tax = total_sales * 0.04
    # Display state sales tax
    print("The state sales tax was", format(state_tax, ',.0f'), "$")
    
    # Total sales tax (county plus state)
    total_tax = county_tax + state_tax
    # Display state sales tax
    print("The total sales tax was", format(total_tax, ',.0f'), "$")
     
main()