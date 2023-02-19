# This program gets a string containing a person’s first,
# middle, and last names, and then display their first,
# middle, and last initials. For example, if the user
# enters John William Smith the program should display J. W. S.
def main():
    # Get the first name.
    f_name = input("Enter the first name: ")
    # Get the middle name.
    m_name = input("Enter the middle name: ")
    # Get the last name.
    l_name = input("Enter the last name: ")
    
    # Make initial of first name.
    f_name = f_name[0]
    f_name = f_name.upper()
    # Make first initial of middle name.
    m_name = m_name[0]
    m_name = m_name.upper()
    # Make first initial of last name.
    l_name = l_name[0]
    l_name = l_name.upper()
    
    # Display the initials of first, middle and
    # last name.
    print(f"{f_name}.{m_name}.{l_name}")
    
if __name__ == "__main__":
    main()