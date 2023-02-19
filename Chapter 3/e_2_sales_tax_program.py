# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 05:39:15 2022

@author: Ali
"""

def main():
    # Get the amount of purchase
    purchase = float(input("Please enter the amount of purchase: "))
    # Display purchase 
    print("The purchae was", format(purchase, ',.0f'), "$")
    state_tax_func(purchase)
    county_tax_func(purchase)
    
def state_tax_func(purchase):
    # The state sales tax is 4 percent
    state_tax = purchase * 0.04
    # Display state sales tax
    print("The state sales tax was", format(state_tax, ',.0f'), "$")

def county_tax_func(purchase):
    # The county sales tax is 2 percent
    county_tax = purchase * 0.02
    # Display county sales tax
    print("The county sales tax was", format(county_tax, ',.0f'), "$")

main()
    
