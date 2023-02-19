# Write a program that accepts a sentence as input 
# and converts each word to “Pig Latin.” In one version,
# to convert a word to Pig Latin you remove the first
# letter and place that letter at the end of the word.
# Then you append the string “ay” to the word. Here is
# an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def main():
    # Get the string from user.
    user_string = input("Enter the string: ")

    # Split the string from "space".
    string_list = user_string.split(' ')
    #print(string_list)

    # Create an empty list.
    my_list = []
    
    for item in string_list:
        if len(item) == 1:
            item = item + "AY"
        else:
            item = item[1:] + item[0] + "AY"
        my_list.append(item)
    
    # Display the items of 'my_list':
    for item in my_list[:-1]:
        print(item, end='')
        print(' ', end='')
    print(my_list[-1])
        
    
                    
if __name__ == "__main__":
    main()           
               
        