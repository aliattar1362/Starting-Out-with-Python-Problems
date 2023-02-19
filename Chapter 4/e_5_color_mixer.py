# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:29:48 2022

@author: Ali

The colors red, blue, and yellow are known as the primary colors because they cannot be
made by mixing other colors. When you mix two primary colors, you get a secondary color,
as shown here: 
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to mix.
If the user enters anything other than “red,” “blue,” or “yellow,” the program
 should display an error message. Otherwise, the program should display the name
 of the secondary color that results. 
"""
# Define the main function.
def main():
    # Get the names of two primary colors to mix.
    first_color = input('Enter the first primary color: ')
    second_color = input('Enter the second primary color: ')
    
    
    # Call the function (color_mixer_func) to determine the final generated color.
    color_mixer_func(first_color, second_color)
        
# Define the function to to determine the final generated color.
def color_mixer_func (color_1, color_2):
     
    # Define the proper condition based input colors.
        
    if ((color_1 == 'yellow' and color_2 == 'red') or 
          (color_2 == 'yellow' and color_1 == 'red')):
        print('When you mix red and yellow, you get orange.')
        
    elif ((color_1 == 'yellow' and color_2 == 'blue') or 
          (color_2 == 'yellow' and color_1 == 'blue')):
        print('When you mix blue and yellow, you get green.')
        
    elif ((color_1 == 'red' and color_2 == 'blue') or 
          (color_2 == 'red' and color_1 == 'blue')):
        print('When you mix red and blue, you get purple.')
        
    else: 
        print('Error: The enterd color is not correct!')


# Call the main function.    
main()
        
        
        
    

