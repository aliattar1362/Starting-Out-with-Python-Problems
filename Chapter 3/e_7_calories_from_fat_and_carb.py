# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:10:34 2022

@author: Ali

A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams * 4
The nutritionist asks you to write a program that will make these calculations.
"""

def main():
    # Get the amount of consumed fat and crabs
    fat = float(input("Please enter the amount of consumed fat in your daily diet: "))
    carb = float(input("Please enter the amount of consumed carbs in your daily diet: "))
    cal_func(fat, carb)
    
def cal_func(fat, carb):
    cal_fat = fat * 9
    cal_carb = carb * 4
    print("You get", format(cal_fat, ',.0f'),"calories from fat and", format(cal_carb, ',.0f'),
          "calories from carbs")
main()