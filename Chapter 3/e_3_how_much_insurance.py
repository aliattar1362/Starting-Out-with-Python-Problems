# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:50:27 2022

@author: Ali
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a
program that asks the user to enter the replacement cost of a building and then displays
the minimum amount of insurance he or she should buy for the property.

"""

def main():
    # Get the replacement cost of a building
    rep_cost = int(input("Please enter the replacement cost of builiding: "))
    rep_cost_func(rep_cost)

def rep_cost_func(price):
    # The minimum amount of insuranc is 80 percent its worth
    min_ins = price * 0.8
    print("The minimimum amount of bulding insurance is", format(min_ins, ',.0f'),"$")
    
main()