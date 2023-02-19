# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:23:40 2022

@author: Ali

There are three seating categories at a stadium. For a softball game, Class A seats cost $15,
Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many tickets
for each class of seats were sold, and then displays the amount of income generated from
ticket sales.
"""
def main():
    # Get the number of sold tickets for each classes
    class_a = int(input("Please enter the number of seats were sold for class A: "))
    class_b = int(input("Please enter the number of seats were sold for class B: "))
    class_c = int(input("Please enter the number of seats were sold for class C: "))
    
    income_func(class_a, class_b, class_c)
    
def income_func(class_a, class_b, class_c):
    income = class_a * 15 + class_b * 12 + class_c * 9
    print("The income was", format(income, ',.0f'), "$")
    
main()