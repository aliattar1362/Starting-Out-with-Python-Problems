# This program lets the user enter the 
# name of a team and then displays the number
# of times that team has won the World Series in 
# the time period from 1903 through 2009.

def main():
    # Open and read the text file.
    infile = open("WorldSeriesWinners.txt", "r")
    # Make an empty list to keep the data
    # of each line.
    champtions_list = []
    
    # Foor loop to create the list of champions.
    for line in infile:
        # Remove '\n' from the rigth end
        # of each line
        line = line.rstrip('\n')
        # Add line to list. 
        champtions_list.append(line)
        
    # Close the file.
    infile.close()
        #line = line.strip()
        
    # initialize the value for total sum
    total = 0
    for item in champtions_list:
        #print(item)
        a = "St. Louis Cardinals" in item
        if a == True:
            total += 1
    print(total)
        
# Call the main function.
if __name__ == "__main__":
    main()
        
