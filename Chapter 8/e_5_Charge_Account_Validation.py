# This program reads the contents of the file into a list. 
# The program asks the user to enter a charge account number. 
# The program determines whether the number is 
# valid by searching for it in the list. If the number 
# is in the list, the program displays a message indicating 
# the number is valid. If the number is not in the list, 
# the program should display a message indicating the number
# is invalid.

def list_creator():
    # Read the contents of text file.
    infile = open("charge_accounts.txt", "r")
    
    # Create an empty list to keep the numbers of file.
    my_list = []
    
    # Add numbers inside the list using for loop.
    for line in infile:
        # Remove '\n' form the end rigth of line.
        line = line.rstrip('\n')
        # Convert the line content to int format.
        line = int(line)
        # Add the content of line to list.
        my_list.append(line)
    
    # Close the infile.
    infile.close()
    
    # Display the content of list.
    #print(my_list)
    return my_list
###################################################################################

def search_func(my_list, number):
    # Search the number in list using for loop.
    ans = number in my_list
    
    # Define the conditoin to display presence of number
    # inside the list.
    if ans == True:
        print("The entered number is valid!")
        
    else:
        print("The entered number is invalid!")
###################################################################################       
    

def main():
    # Call the function to make a list based on text file.
    my_list = list_creator()
    
    # Ask user to enter the seven-digit number.
    number = int(input("Enter the seven-digit number: "))
    
    # Call the fucntion to determine the number is
    # valid or not.
    search_func(my_list, number)
    
# Call the main function.
if __name__ == "__main__":
    main()