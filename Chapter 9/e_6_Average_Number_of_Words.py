# If you have downloaded the source code from this book’s 
# companion Web site, you will
# find a file named text.txt in the Chapter 09 folder. 
# The text that is in the file is stored
# as one sentence per line. Write a program that reads
# the file’s contents and calculates the
# average number of words per sentence.

def main():
    # Read the file named text.txt.
    infile = open("text.txt", 'r')
    
    # Counter for lines.
    li_counter = 0
    total_letter = 0
    for line in infile:
        line = line.rstrip('\n')
        line_list = line.split(' ')
        
        # Initialize a list counter.
        le_counter = 0
        total_le_per_line = 0
        while not le_counter == len(line_list):
            total_le_per_line += len(line_list[le_counter])
            le_counter += 1
        li_counter += 1
        total_letter += total_le_per_line
        #print(total_le_per_line)
    # Close the file
    infile.close()
    
    print(total_letter)
    print(li_counter)

# Call the main function    
if __name__ == "__main__":
    main() 