# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:46:07 2022

@author: Ali

Write a program that calculates and displays a person’s body mass index (BMI). The
BMI is often used to determine whether a person is overweight or underweight for his
or her height. A person’s BMI is calculated with the following formula:
BMI weight 703 / height^2
where weightis measured in pounds and heightis measured in inches.
"""

def main():
    # get the user's weight and height in pounds and inches, respectively.
    weight = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))
    bmi_func(weight, height)
    
def bmi_func(weight, height):
    bmi = (weight * 703) / (height ** 2)
    print("Your BMI is", format(bmi, ',.2f'))
    
main()

