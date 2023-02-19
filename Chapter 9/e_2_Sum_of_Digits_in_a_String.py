# This program asks the user to enter a series
# of single-digit numbers with nothing separating
# them. The program should display the sum of
# all the single digit numbers in the string. 
# For example, if the user enters 2514, the 
# method should return 12, which is the sum 
# of 2, 5, 1, and 4.

def main():
    # Get the number
    number = input("Enter the number: ")
    
    # Initialize the sum of numbers
    total = 0
    
    # Use for loop to sum up the digits.
    for num in number:
        num = int(num)
        total += num
    print("The sum of number's digits is:", total) 

# Call the main function    
if __name__ == "__main__":
    main()