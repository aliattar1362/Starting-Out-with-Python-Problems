# This function make a text file containing a series of names
# by asking user to enter these names.
def name_maker():
    # Make the names.txt file
    names_file = open("names.txt", "w")
    
    # Prompt the user to enter the first desire name
    print("Enter the names on each line:")
    line = input("")
    
    while not line == "":
        names_file.write(line + '\n')
        line = input("")
        
    names_file.close()
    
##########################################################

# This function called text file and count the 
# number of names.
def name_counter():
    # Call the text file.
    my_file = open("names.txt", "r")
    
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
    
    # Print the number of names
    print("The number of names in 'names.txt' ", end="")
    print(f"file is {counter}.")
##########################################################

# Define main function to call both name_maker() and
# name_counter() fucntions.
def main():
    # Call name_maker fucntion to make a text file 
    # to get names from user.
    name_maker()
    # Call name_counter fucntion to count number of names
    # in list.
    name_counter()
    
if __name__ == "__main__":
    main()
    
        
    
      






# 