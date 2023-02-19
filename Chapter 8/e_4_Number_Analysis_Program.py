# This program asks the user to enter a series of 20 numbers. 
# This program stores the numbers in a list and displays the 
# following data:
    # .The lowest number in the list
    # .The highest number in the list
    # .The total of the numbers in the list
    # .The average of the numbers in the list

import random

def main():
    # A constant variable for length of list.
    LEN_LIST = 20
    
    # An empty list to keep the numbers.
    my_list = []
    
    # Initialize the total value.
    total = 0
    
    # Use a loop to generate the random numbers and keep them
    # inside the list.
    for num in range(LEN_LIST):
        # Generate the random number in desired range.
        number = random.randrange(1, 21)
        # Put the number into the list.
        my_list.append(number)
        # Accumulate the number in total.
        total += number
        
    # Display the list
    print(my_list)
        
    # Find and display the lowest number in the list.
    lowest_number = min(my_list)
    print("The lowest number in the list is ",\
         lowest_number, ".", sep="")
        
    # Find and display the highest number in the list.
    highest_number = max(my_list)
    print("The highest number in the list is ",\
         highest_number, ".", sep="")
        
    # Display the total value of numbers of the list.
    print("The total of numbers in the list is ",\
         total, ".", sep="")
        
    # Calculate and display the average value of 
    # numbers of the list.
    ave = total/LEN_LIST
    print("The average of numbers in the list is ",\
          format(ave, '0.2f'), ".", sep="")
        
# Call the main function.
if __name__ == "__main__":
    main()        
    
    
    