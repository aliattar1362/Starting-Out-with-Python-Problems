# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:56:16 2022

@author: Ali

Write a program that asks the user to enter five test scores. The program should display a letter
grade for each score and the average test score. Write the following functions in the program:
• calc_average—This function should accept five test scores as arguments and return
the average of the scores.
• determine_grade—This function should accept a test score as an argument and
return a letter grade for the score, based on the following grading scale:
Score       Letter Grade
90–100      A
80–89       B
70–79       C
60–69       D
Below 60    F
"""
# Global variable for number os grades
NUM_GRADES = 5

def main():
    # Constant to initalize the total
    total = 0
    
    for score in range(1, NUM_GRADES+1):
        print('Enter the score for course', score, end='')
        test_score = int(input(' here: '))
        grade = determine_grade(test_score)
        print('Your grade for', test_score, 'is', grade)
        total += test_score
        
    average = calc_average(total)
    print('The average of', NUM_GRADES, 'entered grades is', format(average, ',.0f'))
        
    
def calc_average(total):
    average = total/NUM_GRADES
    return average
    
def determine_grade(score):
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = 'C'
    elif score >= 60 and score <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade
    
main()    