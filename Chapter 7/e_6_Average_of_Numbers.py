# This function called text file and count the 
# amount of numbers.
def numbers_counter():
    # Call the text file.
    my_file = open("numbers.txt", "r")
    
    # Read the first line
    line = my_file.readline()
    
    # Define the condition for line. It should
    # be a filled line
    counter = 0
    while not line == "":
        # Sum the counter.
        counter += 1
        # Call the next line
        line = my_file.readline()
        
    # Close the file.   
    my_file.close()
    # Return the count of numbers in file.
    return counter
    
##########################################################

# This function called text file and calculate the 
# total of numbers.
def total_numbers_calculater():
    # Call the text file.
    my_file = open("numbers.txt", "r")
    
    # Read the first line
    line = my_file.readline()
    
    # Define the condition for line. It should
    # be a filled line containig a number.
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
    
    # Return the total of numbers in list.
    return total
    

##########################################################

# Define main function to call both name_maker() and
# name_counter() fucntions.
def main():
    # Call numbers_text_maker fucntion to make a text file 
    # to get numbers from user.
    count = numbers_counter()
    # Call name_counter fucntion to count number of names
    # in list.
    total = total_numbers_calculater()
    # Calculate the average of numbers in file.
    ave = total/count
    # Displays the average of numbers in text file.
    print("The average of numbers in ", end = "")
    print(f"'numbers.txt' file is {ave:0.2f}.")
    
if __name__ == "__main__":
    main()
    
        
    
      






# 