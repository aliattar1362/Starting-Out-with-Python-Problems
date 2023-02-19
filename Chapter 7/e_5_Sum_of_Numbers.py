# This function make a text file containing a series of numbers
# by asking user to enter these numbers.
def numbers_text_maker():
    # Make the numbers.txt file
    names_file = open("numbers.txt", "w")
    
    # Prompt the user to enter the first desire name
    print("Enter the numbers on each line:")
    line = input("")
    
    while not line == "":
        names_file.write(line + '\n')
        line = input("")
        
    names_file.close()
    
##########################################################

# This function called text file and calculate the 
# total of numbers.
def numbers_calculater():
    # Call the text file.
    my_file = open("numbers.txt", "r")
    
    # Read the first line
    line = my_file.readline()
    
    # Define the condition for line. It should
    # be a filled line
    total = 0
    while not line == "":
        # Eliminate '\n' from the end rigth of text.
        line = line.rstrip('\n')
        # Convert the line format to int.
        line = int(line)
        # Sum the counter.
        total += line
        # Call the next line
        line = my_file.readline()
        
    # Close the file.   
    my_file.close()
    
    # Print the number of names
    print("The total of numbers in 'numbers.txt' ", end="")
    print(f"file is {total}.")
##########################################################

# Define main function to call both name_maker() and
# name_counter() fucntions.
def main():
    # Call numbers_text_maker fucntion to make a text file 
    # to get numbers from user.
    numbers_text_maker()
    # Call name_counter fucntion to count number of names
    # in list.
    numbers_calculater()
    
if __name__ == "__main__":
    main()
    
        
    
      






# 