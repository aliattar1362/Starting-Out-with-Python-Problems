# -*- coding: utf-8 -*-
"""
Assume that a file containing a series of integers is 
named numbers.txt and exists on the computer’s disk. 
Write a program that displays all of the numbers in the file.
"""

# This program calls text file named numbers.txt
# and display the data that is included numbers

def main():
    # Calling the file
    my_file = open("numbers.txt", "r")
    
    # Read the content of first line
    line = my_file.readline() 
    
    # Define the condition for line
    # If the line is not empty shows the line
    while not line == '' :
        # Convert the line format to int.
        line = int(line)
        
        # Print the data of the line
        print(line)
        
        # Get the data in next line
        line = my_file.readline() 
        
    my_file.close()   
    
#call the main function
if __name__ == "__main__":
    main()
        
    
