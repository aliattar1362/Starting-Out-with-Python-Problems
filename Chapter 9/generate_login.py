# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    id_num = input("Enter the ID number: ")
    
    # Get the login name.
    print('Your system login name is:')
    print(login.get_login_name(first, last, id_num))
    
# Call the main function.
main()
    
    
    
