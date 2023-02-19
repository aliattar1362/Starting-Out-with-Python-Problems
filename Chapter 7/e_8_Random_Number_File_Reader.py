# This fucntion is called the random "random_numbers.txt" 
# file and display its content. 
def show_file():
    # Call the file.
    my_file = open("random_numbers.txt", "r")
    print(my_file.read())
    
    my_file.close()
###########################################################################

# This function called text file and calculate the 
# total of numbers.
def total_numbers_calculater():
    # Call the text file.
    my_file = open("random_numbers.txt", "r")
    
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
###########################################################################

# This function called text file and count the 
# amount of numbers.
def numbers_counter():
    # Call the text file.
    my_file = open("random_numbers.txt", "r")
    
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
###########################################################################

# Define the main function.
def main():
    # Call the fucntion to show the file.
    show_file()
    # Call the function to show the calculated 
    # total of numbers in file.
    total = total_numbers_calculater()
    # Display the total.
    print('The total of numbers ', end = "")
    print('in "random_numbers.txt" ', end = "")
    print(f"file is {total:0.0f}.")
    
    # Call the function to count the number of
    # numbers in text file.
    count = numbers_counter()
    print('The amount of numbers ', end = "")
    print('in "random_numbers.txt" ', end = "")
    print(f"file is {count}.")
    
if __name__ == "__main__":
    main()