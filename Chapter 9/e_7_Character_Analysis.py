# If you have downloaded the source code from this 
# book’s companion Web site, you will find a file 
# named text.txt in the Chapter 09folder. Write a 
# program that reads the file’s contents and 
# determines the following:
#• The number of uppercase letters in the file
#• The number of lowercase letters in the file
#• The number of digits in the file
#• The number of whitespace characters in the file

def main():
    # Read the text file.
    infile = open("text.txt", 'r')
    
    # Initialize total counter for number of uppercase 
    # letter, lowercase letter, digits, and  
    # spaces inside the text.
    total_upper = 0
    total_lower = 0
    total_digit = 0
    total_space = 0
    
    # For loop is used to remove '\n' from 
    # end of each line, split text from space (' ')
    # that lead to creating list of each line.
    for line in infile:
        line = line.rstrip('\n')
        line_list = line.split(' ')
        
        # Initialize a counter for words in each line 
        # of the list.
        word_counter = 0
        uppercase_counter = 0
        lowercase_counter = 0
        digit_counter = 0
        
        # Define conditions to calculate number 
        #  of desired objects.
        while not word_counter == len(line_list):
            for ch in line_list[word_counter]:
                if ch.isupper():
                    uppercase_counter += 1
                if ch.islower():
                    lowercase_counter += 1
                if ch.isdigit():
                    digit_counter += 1
            word_counter += 1
            
        # Display the total number of desired objects.
        total_upper += uppercase_counter
        total_lower += lowercase_counter
        total_digit += digit_counter
        # Spaces are 1 more less than number of words
        # in each line.
        total_space += word_counter-1
            
    # Close the file
    infile.close()
    
    # Display the desired objects.
    print("The total number of uppercase letters " +
          f"in whole text are {total_upper}.")
    print("The total number of lowercase letters " +
          f"in whole text are {total_lower}.")
    print("The total number of digits " +
          f"in whole text are {total_digit}.")
    print("The total number of spaces " +
          f"in whole text are {total_space}.")

# Call the main function    
if __name__ == "__main__":
    main() 