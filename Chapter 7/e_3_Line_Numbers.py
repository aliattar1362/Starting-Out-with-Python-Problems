# This programs asks the user to enter name of a file. 
# Then it shows the content of each line proceed with a
# line number starts at 1, followed by a colon.

def main():
    # Enter the name of desired file to be called
    print("Enter the name of text file ", end="")
    print("including the format:", end="")
    file = input("for example (file.txt): ")
    
    # Call the file in reading format
    my_file = open(file, "r")
    
    # Read the first line
    line = my_file.readline()
    
    # Define the number to be print for first line
    number = 1
    # Define a condition to print the contensts of lines
    # according to requested condition
    while not line == "":
        # Eliminate the '\n' from the end rigth of lines
        line = line.rstrip('\n')
        # Show the contents of each line including 
        # the line number
        print(number , ". ", line, sep ="")
        # Increasing the number for next line
        number += 1
        # Read the next line
        line = my_file.readline()
    
    # Close the file
    my_file.close()   
    
# Call the main function
if __name__ == "__main__":
    main()
    
    