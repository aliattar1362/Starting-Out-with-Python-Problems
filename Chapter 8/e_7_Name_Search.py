def list_maker(text_file):
    # Call text file in reading mode.
    infile = open(text_file, "r")
    
    # Initialize an empty list.
    my_list = []
    
    for line in infile:
        # Remove '\n' form the end rigth of line.
        line = line.rstrip('\n')
        # Add the content of line to list.
        my_list.append(line)
    
    # Close the infile.
    infile.close()
    
    # Return the list to main function.
    return my_list

###################################################################################

def search_func(my_list, name):
    # Search the number in list using for loop.
    ans = name in my_list
    
    # Define the conditoin to display presence of number
    # inside the list.
    if ans == True:
        print(f"Yes, Yes! The {name} is inside the list!")
        
    else:
        print(f"Sadly the {name} is not inside the list!")
###################################################################################   

def search_in_girl_list():
    print("Do you want to search for a name of girl ", end='')
    sea_in_girl = input("('y')? ")
    if sea_in_girl == 'y':
        # Call the list_maker() fucntino to generate the list of
        # popular names of girls.
        girl_list = list_maker("GirlNames.txt")
        # Get the name of girl.
        girl_name = input("Enter the name of girl: ")
        # Call the search fucntion.
        search_func(girl_list, girl_name)
###################################################################################
def search_in_boy_list():
    print("Do you want to search for a name of boy ", end='')
    sea_in_boy = input("('y')? ")
    if sea_in_boy == 'y':
        # Call the list_maker() fucntino to generate the list of
        # popular names of boys.
        boy_list = list_maker("BoylNames.txt")
        # Get the name of boy.
        boy_name = input("Enter the name of boy: ")
        # Call the search fucntion.
        search_func(boy_list, boy_name)


###################################################################################
    
    
def main():
    # Get the text file.
    print("Enter the name of text file with text format (.txt)")
    text_file = input(": ")
    my_list  = list_maker(text_file)
    
    # Get the name for search in list.
    name = input("Enter desired name inside text file: ")
    # Call the search function.
    search_func(my_list, name)


# Call the main function.
if __name__ == "__main__":
    main()    

    
    
    
    
    