# Write a program that uses a dictionary to assign “codes”
# to each letter of the alphabet. For example:
# codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
# Using this example, the letter A would be assigned the 
# symbol %, the letter a would be assigned the number 9,
# the letter B would be assigned the symbol @, and so forth.
# The program should open a specified text file, read its
# contents, and then use the dictionary to write an encrypted
# version of the file’s contents to a second file. Each character
# in the second file should contain the code for the corresponding
# character in the first file. Write a second program that 
# opens an encrypted file and displays its decrypted contents on
# the screen.

def main():
    
    
    
    codes = { 'A' : '!', 'a' : '1 ', 'B' : '@', 'b' : '2 ',
             'C' : '#', 'c' : '3 ', 'D' : '¤', 'd' : '4 ',
             'E' : '%', 'e' : '5 ', 'F' : '&', 'f' : '6 ',
             'G' : '/', 'g' : '7 ', 'H' : '(', 'h' : '8 ',
             'I' : ')', 'i' : '9 ', 'J' : '=', 'j' : '10 ',
             'K' : '?', 'k' : '11 ', 'L' : '^', 'l' : '12 ',
             'M' : '*', 'm' : '13 ', 'N' : 'Ä', 'n' : '14 ',
             'O' : 'Ö', 'o' : '15 ', 'P' : '-', 'p' : '16 ',
             'Q' : '_', 'q' : '17 ', 'R' : '.', 'r' : '18 ',
             'S' : ':', 's' : '19 ', 'T' : ',', 't' : '20 ',
             'U' : ';', 'u' : '21 ', 'V' : '<', 'v' : '22 ',
             'W' : '>', 'w' : '23 ', 'X' : '$', 'x' : '24 ',
             'Y' : '{', 'y' : '25 ', 'Z' : '+', 'z' : '26 '}
    
    text = "On on produce colonel pointed. Just four sold need \
    over how any."
    
    rev_text = 'Ö14 .15 14 .16 18 15 4 21 3 5 .3 15 12 15 14 5 \
    12 .16 15 9 14 20 5 4 .=21 19 20 .6 15 21 18 .19 15 12 4 \
        .14 5 5 4 .....15 22 5 18 .8 15 23 .1 14 25 '
    
    for ch in text:
        if ch in codes:
            print(codes[ch], end='')
            
        elif ch ==' ':
            print('.', end='')
        
    key_list = []
    value_list = []
    
    for key in codes.keys():
        key_list.append(key)
    
    #print(key_list)
    
    for value in codes.values():
        value_list.append(value)
    
    #print(value_list)
    
    for ch in rev_text:
        if ch in value_list:
            index = value_list.index(ch)
            print(key_list[index], end='')
        
        elif ch == '.':
            print(' ', end='')
            

                
main()