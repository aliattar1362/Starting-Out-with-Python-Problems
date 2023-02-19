# -*- coding: utf-8 -*-
"""
Write a program that asks the user for the name of a file. 
The program should display only the first five lines of 
the file’s contents. If the file contains less than five lines, 
it should display the file’s entire contents.
"""

# This program calls a text file by asking the user to write the
# name of file. Then, prints the first five lines of the text
# file. If the number of lines are less than five, it displays
# the file’s entire contents.

def main():
    
    # Prompt the name of text file from the user
    print("Enter the name of text file including the format:")
    file_name = input("for example (file.txt): ")
    
    # Calling the file
    my_file = open(file_name, "r")

    # Define a condition to print lines of called file.
    # This condition prints the lines up to fifth. 
    counter = 0
    while not counter == 5:
        line = my_file.readline()
        line = line.rstrip('\n')
        print(line)
        counter += 1

    # Close the file.
    my_file.close()
        
#call the main function
if __name__ == "__main__":
    main()
        
    
