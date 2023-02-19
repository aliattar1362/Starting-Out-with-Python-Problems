# Many companies use telephone numbers like 555-GET-FOOD
# so the number is easier for their customers to 
# remember. On a standard telephone, the alphabetic 
# letters are mapped to numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9
# This program asks the user to enter a 10-character 
# telephone number in the format XXX-XXX-XXXX. 
# The application should display the telephone number 
# with any alphabetic characters that appeared in the 
# original translated to their numeric equivalent. For
# example, if the user enters 555-GET-FOOD 
# the application should display 555-438-3663.
def alph_to_num_conventor(string):
    # Initialize a list to keep the output.
    my_list = []
    
    # Use for loop to convert alphs to digits.
    for ch in string:
        if ch == "A" or ch == "B" or ch == "C":
            ch = 2
        elif ch == "D" or ch == "E" or ch == "F":
            ch = 3
        elif ch == "G" or ch == "H" or ch == "I":
            ch = 4
        elif ch == "J" or ch == "K" or ch == "L":
            ch = 5
        elif ch == "M" or ch == "N" or ch == "O":
            ch = 6
        elif ch == "P" or ch == "Q" or ch == "R":
            ch = 7
        elif ch == "T" or ch == "U" or ch == "V":
            ch = 8
        elif ch == "W" or ch == "X" or ch == "Y" or ch == "Z":
            ch = 9
            
        my_list.append(ch)

    # Return the list
    return my_list
    
def main():
    # Get the 10-character telephone number in 
    # the format XXX-XXX-XXXX.
    print("Enter a 10-character telephone number", end='')
    tel_num = input("in the format XXX-XXX-XXXX: ")
    
    tel_num_list = tel_num.split('-')
    print(tel_num_list)
    
    set_1 = tel_num_list[0]
    set_2 = alph_to_num_conventor(tel_num_list[1])
    set_3 = alph_to_num_conventor(tel_num_list[2])
    
    print(set_1, '-', sep= '', end='')
    
    for num in set_2:
        print(num, end='')
    print('-', end='')
    
    for num in set_3:
        print(num, end='')
    
# Call the main function    
if __name__ == "__main__":
    main() 