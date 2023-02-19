# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 07:47:34 2022

@author: Ali

Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 5 points.
• If a customer purchases 2 books, he or she earns 15 points.
• If a customer purchases 3 books, he or she earns 30 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she
 has purchased this month and displays the number of points awarded.
"""
# Define the main function.
def main():
    # Ask user to enter the number of books that he or she has purchased this month.
    books = int(input('Enter the number of books you have purchased this month: '))
    
    # Call the function (points_awarded_func) to displays the number of points awarded.
    points_awarded_func(books)
        
# Define the function to to determine the user win the game or not.
def points_awarded_func (num):
  
    # Define the proper condition based on numbers of purchased books.
    if num == 0:
        print('You earn 0 points!')
    elif num == 1:
        print('You earn 5 points!')
    elif num == 2:
        print('You earn 15 points!')
    elif num == 3:
        print('You earn 30 points!')
    else: 
        print('You earn 60 points!')

# Call the main function.    
main()
        
        

