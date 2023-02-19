# This proram makes a text file named "charge_accounts.txt" 
# containg 20 seven-digit number.
import random

def main():
    # Make a text file.
    outfile = open("charge_accounts.txt", "w")
    
    # Create 20 seven-digit random number.
    for l in range(20):
        for num in range(7):
            number = random.randrange(1, 10)
            outfile.write(str(number))
        
        # Go to next line for next seven-digit.
        outfile.write('\n')
        
    # Close the outfile.
    outfile.close()
    
# Call the main function.
if __name__ == "__main__":
    main() 
            
            
    
    