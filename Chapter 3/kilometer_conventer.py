# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    
    # Get the distance in kilometer
    distance = int(input("Please enter the distance in kilometers: "))
    convert_to_mile(distance)
    
def convert_to_mile(kilometers):
    miles = kilometers * 0.6214
    print("Distance is", format(miles, ',.2f'), "miles.")
        
main()