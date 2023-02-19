# Morse code is a code where each letter of the 
# English alphabet, each digit, and various
# punctuation characters are represented by a 
# series of dots and dashes. Table 9-5 shows part
# of the code. this program asks the user to enter 
# a string, and then converts that string to Morse
# code.

def main():
    # Get the string from the user.
    user_string = input("Enter a string: ")
    # Make an empty list.
    mores_list = []
    
    # Put the charachter of string to list
    # using for loop.
    for ch in user_string:
        ch = ch.upper()
        
        # Determine the condition for coding
        # rules of Morse characters.
        if ch == " ":
            ch = " "
        elif ch == ",":
            ch = "– – . . – –"
        elif ch == ".":
            ch = ". – . – . –"
        elif ch == "?":
            ch = ". . – – . ."
        elif ch == "0":
            ch = "– – – – –"
        elif ch == "1":
            ch = ". – – – –"
        elif ch == "2":
            ch = ". . – – –"
        elif ch == "3":
            ch = ". . . – –"
        elif ch == "4":
            ch = ". . . . –"
        elif ch == "5":
            ch = ". . . . ."
        elif ch == "6":
            ch = "– . . . ."
        elif ch == "7":
            ch = "– – . . ."
        elif ch == "8":
            ch = "– – – . ."
        elif ch == "9":
            ch = "– – – – ."
        elif ch == "A":
            ch = ". –"
        elif ch == "B":
            ch = "– ..."
        elif ch == "C":
            ch = "– . – ."
        elif ch == "D":
            ch = "– . ."
        elif ch == "E":
            ch = "."
        elif ch == "F":
            ch = ". . – ."
        elif ch == "G":
            ch = "– – ."
        elif ch == "H":
            ch = "...."
        elif ch == "I":
            ch = ".."
        elif ch == "J":
            ch = ". – – –"
        elif ch == "K":
            ch = "– . –"
        elif ch == "L":
            ch = ". – . ."
        elif ch == "M":
            ch = "– –"
        elif ch == "N":
            ch = "– ."
        elif ch == "O":
            ch = "– – –"
        elif ch == "P":
            ch = ". – – ."
        elif ch == "Q":
            ch = "– – . –"
        elif ch == "R":
            ch = ". – ."
        elif ch == "S":
            ch = ". . ."
        elif ch == "U":
            ch = ". . –"
        elif ch == "V":
            ch = "...–"
        elif ch == "W":
            ch = ". – –"
        elif ch == "X":
            ch = "– . . –"
        elif ch == "Y":
            ch = "– . –"
        elif ch == "Z":
            ch = "– – . ."
            
        mores_list.append(ch)
    
    # Display the content of Mores list
    # using for loop.
    for item in mores_list:
        print(item, end='')
    
# Call the main function    
if __name__ == "__main__":
    main()    