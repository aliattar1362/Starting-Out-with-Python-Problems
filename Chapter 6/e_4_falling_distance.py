# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:09:01 2022

@author: Ali

The following formula can be used to determine the distance an object falls due to gravity
in a specific time period, starting from rest:
d = 1⁄2 g(t**2)
The variables in the formula are as follows: dis the distance in meters, g is 9.8, 
and t is the amount of time in seconds, that the object has been falling.
Write a function named 'falling_distance' that accepts an object’s falling time in seconds
as an argument. The function should return the distance in meters that the object
 has fallen during that time interval. Write a program that calls the function
 in a loop that passes the values 1 through 10 as arguments and displays the return value.
"""
def main():
    # define constants for first and last time in interval. 
    FIRST_TIME = 1
    LAST_TIME = 10
    for time in range(FIRST_TIME, LAST_TIME + 1):
        d = falling_distance(time)
        print('After', time, 's, the distance is', format(d, ',.2f'), 'meters.')
        
    
def falling_distance(t):
    # The constant for gravity acceleration in (m/s**2)
    g = 9.8 
    # The formula d = 1⁄2 g(t**2)
    d = 1/2 * g * (t**2)
    return d
main()