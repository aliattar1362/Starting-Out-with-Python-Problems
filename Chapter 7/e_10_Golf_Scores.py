# This function asks the  player’s name and golf score
# and save them in a file named golf.txt
def golf_data_saver():
    # Create the file.
    my_file = open("golf.txt", "w")
    
    # Ask for name of the first player.
    name = input("Enter the name of the next golf player: ")
    # Ask for score of the first player.
    score = input("Enter the score of the next golf player: ")
    
    while not name == "":
        my_file.write(str(f"{name:<10}") + str(f"{score:>10}") + '\n')

        # Ask for next name and score of the first player.
        name = input("Enter the name of the first golf player: ")
        score = input("Enter the score of the first golf player: ") 

    # Close the file.
    my_file.close()
#############################################################################################

# this functino displays the data in "golf.txt" file.
def show_data():
    # Create the file.
    my_file = open("golf.txt", "r")
    
    # Define for loop to display the data from the text file.
    for line in my_file:
        line = line.rstrip('\n')
        print(line)

    # Close the file.
    my_file.close()
#############################################################################################

# This is the main function
def main():
    # Call the fucntion to make the "golf.txt" file.
    golf_data_saver()
    
    # Call the fucntion to display the data inside 
    # the "golf.txt" file.
    show_data()
    
if __name__ == "__main__":
    main()      
    
    