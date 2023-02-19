import random

# This function make a text file containing a series of random 
# numbers by asking user to enter the number of these numbers.
def random_numbers_maker():
    # Make the numbers.txt file
    random_numbers_file = open("random_numbers.txt", "w")
    
    # Prompt the user to enter the amount of random numbers.
    amount = int(input("Enter the amount of random numbers: "))
    # Define for loop to make file.
    for n in range(amount):
        # Create the random int in range of 1 to 100.
        random_number = random.randrange(1,101)
        # Add the random number to the file. The format of number
        # shoule be converted to str to be written in file.
        random_numbers_file.write(str(random_number) + '\n')
        
    # Close the file
    random_numbers_file.close()
###########################################################################

# Define the main function
def main():
    # Call the random numbers file function.
    random_numbers_maker()
    
if __name__ == "__main__":
    main()