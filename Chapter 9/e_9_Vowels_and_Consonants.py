# Write a program with a function that accepts a string 
# as an argument and returns the number of vowels that 
# the string contains. The application should have 
# another function that accepts a string as an argument 
# and returns the number of consonants that the string 
# contains. The application should let the user enter 
# a string and should display the number of vowels and 
# the number of consonants it contains.

def vowel_counter(argument):
    argument_list = argument.split(' ')
    
    # Initialize counter for vowel sound.
    counter = 0
    # Use for loop to count the number of vowel 
    # sound in argument.
    for item in argument_list:
        for ch in item:
            # Convert the character to lowercase
            # letter
            ch = ch.lower()
            # Check if the character is vowel.
            if ch in ('a', 'e', 'i', 'o', 'u'):
                # If yes increase the counter.
                counter += 1

    # Display the number of vowels inside
    # the string.
    print(f"There are {counter} vowels inside " + 
          "the argument.")
#######################################################################

def consonant_counter(argument):
    argument_list = argument.split(' ')
    
    # Initialize counter for consonant sound.
    counter = 0
    # Use for loop to count the number of consonant 
    # sound in argument.
    for item in argument_list:
        for ch in item:
            # Convert the character to lowercase
            # letter
            ch = ch.lower()
            # Check if the character is vowel.
            if not ch in ('a', 'e', 'i', 'o', 'u'):
                # If yes increase the counter.
                counter += 1
    
    # Display the number of consonants inside
    # the string.
    print(f"There are {counter} consonants inside " + 
          "the argument.")
#######################################################################
   
def main():
    # Get the argument.
    arg = input(" Enter the argument here: ")
    
    vowel_counter(arg)
    consonant_counter(arg)
    
if __name__ == "__main__":
    main()           
            
    