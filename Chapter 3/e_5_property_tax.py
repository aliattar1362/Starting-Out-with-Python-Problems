# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:20:39 2022

@author: Ali

A county collects property taxes on the assessment value of property, which is 60 percent of
the property’s actual value. For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then 64¢ for each $100
of the assessment value. The tax for the acre assessed at $6,000 will be $38.40. Write a program that
asks for the actual value of a piece of property and displays the assessment value and
property tax.
"""

def main():
    # Get the actual value of a piece of property
    actual_value = int(input("Please insert the actual value of a piece of property: "))
    ass_value_func(actual_value)
    prop_tax_func(actual_value)
    
def ass_value_func(value):
    assessment_value = value * 0.6
    print("The assessment value of this property is", format(assessment_value,',.0f'), "$")
    
def prop_tax_func(value):
    property_tax = value * 0.6 * 0.0064
    print("The property tax of this property is", format(property_tax,',.2f'), "$")
    
main()