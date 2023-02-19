# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 23:32:48 2022

@author: Ali

Write a program that asks the user to enter a number of seconds, and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should display the number of minutes in that many
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should display the number of hours in that
many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
than or equal to 86,400, the program should display the number of days in that many
seconds.
"""
# Define the main function.
def main():
    # Ask user to enter his/her weight .
    time = int(input('Enter a number of seconds: ')) # Time in seconds
    
    # Call the function (time_func) to calculate and displays the time.
    time_func(time)
        
# Define the function to calculate and displays the time.
def time_func (time):
    days = time // 86400 
    hours = time // 3600 
    minutes = time // 60
     
    # Define the proper condition based on input time.
    if time >= 60 and time < 3600 :
        print('There are', minutes, 'minute/minutes in this time')
    
    elif time >= 3600 and time < 86400 :
        print('There are', hours, 'hour/hours in this time')
    
    elif time >= 86600 :
        print('There are', days, 'day/days in this time')

# Call the main function.    
main()
