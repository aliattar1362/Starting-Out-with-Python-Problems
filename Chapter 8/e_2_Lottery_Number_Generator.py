# This program generates a seven-digit lottery number. 
import random

def main():
    # Global variable for length of lottery number.
    length_lottery_number = 7
    
    # Create an empty list to keep the numbers.
    lottery_list = []
    
    # Make a loop to create seven-digit lottery number.
    for num in range(length_lottery_number):
        number = random.randrange(0,10)
        lottery_list.append(number)
    
    # Make a loop to display created number for lottery number.
    for num in lottery_list:
        print(num, end="")

# Call the main function.        
if __name__ == "__main__":
    main()