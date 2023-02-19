# -*- coding: utf-8 -*-
"""
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same.

"""
# Define the main function.
def main():
    # Get the length and width of first rectangle.
    len_1 = float(input('Enter the length of first rectangle: '))
    wid_1 = float(input('Enter the width of first rectangle: '))
    
    # Get the length and width of second rectangle.
    len_2 = float(input('Enter the length of second rectangle: '))
    wid_2 = float(input('Enter the width of second rectangle: '))
    
    # Call the function (rec_area_func) to calculate the area of first rectangle.
    area_1 = rec_area_func(len_1, wid_1)
    # Call the function (rec_area_func) to calculate the area of second rectangle.
    area_2 = rec_area_func(len_2, wid_2)
    
    # Define the proper condition based on areas of rectangles.
    if area_1 > area_2 :
        print('The area of the first rectangle is greater than the area of the second one.')
    elif area_1 < area_2 :
        print('The area of the second rectangle is greater than the area of the first one.')
    else:
        print('The areas of two rectangles are the same.')
        
    
# Define the function to calculate the area of the rectangle.
def rec_area_func(length, width):
    area = length * width
    return(area)

# Call the main function.    
main()
        
        
        
    
    