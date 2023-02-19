# This program has a function that accepts a string as 
# an argument and returns a copy of the string with the 
# first character of each sentence capitalized. 
# For instance, if the argument is “hello. my name is Joe.
# what is your name?” the function should return the string
# “Hello. My name is Joe. What is your name?” The program
# should let the user enter a string and then pass it to 
# the function. The modified string should be displayed.

def main():
    # Get the string as an argument.
    argument = input("Enter desired text: ")
    
    arg_list = argument.split('. ')
    #print(arg_list)
    
    # Initialize counter for while loop.
    index = 0
    # While loop to Capitalize the first letter of
    # each item inside the list.
    while not index == len(arg_list):
        # Capitalize the items in list.
        arg_list[index] = arg_list[index].capitalize()
        # Increase index number to go to next loop.
        index += 1
    
    # Initialize counter for while loop.
    index = 0
    
    # While loop to display the items inside the list.
    while not index == len(arg_list)-1:
        # Display the items of list except the last item
        # because these are ended with 'period == .'.
        print(f"{arg_list[index]}. ", end='')
        # Increase index number to go to next loop.
        index += 1
    # Display the last items of list.
    print(f"{arg_list[index]}")
    
# Call the main function    
if __name__ == "__main__":
    main() 
    
