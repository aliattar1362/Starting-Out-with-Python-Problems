# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:56:14 2022

@author: Ali

Write a program that gives simple math quizzes. The program should display two random
numbers that are to be added, such as:
  247
+ 129
The program should allow the student to enter the answer. If the answer is correct, 
a message of congratulations should be displayed. If the answer is incorrect, 
a message showing the correct answer should be displayed.
"""
import random

def main():
    first, second = rand_gen_func()
    display_func(first, second)
    user_value = get_input_func()
    result = sum_func(first, second)
    compare_func(user_value, result)
    

    
def display_func(num1, num2):
    print('\t', num1)
    print('+\t', num2)
     
def rand_gen_func():
    first_ran_num = random.randint(100,999)
    second_ran_num = random.randint(100,999)
    return first_ran_num, second_ran_num

def sum_func(num1, num2):
    result = num1 + num2
    return result

def get_input_func():
    user_value = int(input('Enter your answer: '))
    return user_value

def compare_func(user_value, correct_value):
    if user_value != correct_value:
        print('Your answer is wrong. The correct value is', correct_value, '.')
    else:
        print('Congratulations, you enterd the correct value that is', user_value, '.')
        
main()
