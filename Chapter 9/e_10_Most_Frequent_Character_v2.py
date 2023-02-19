# In this version 'dictionary' is used to make 
# more accurate result. For example it can specify 
# several letter with highest repeatition.

def main():
    
    text = 'balloon'
    # Convert all letters to lowercase.
    text = text.lower()
    my_list = text.split(' ')
    # Make an empty dictionary to add letters and their 
    # repatation values to it.
    text = ''
    
    for item in my_list:
        text += item
        
    # Initialize empty dictionary
    my_dic = {}
    
    
    # Use loop to iterate insite the letters in text
    # and add them to the dictionary.
    for ch in text:
        # Increase the value of letter if it is inside the
        # the dictionary
        if ch in my_dic:
            my_dic[ch] += 1
        
        # Add letter to the dictionary and correlate 1 as its value 
        # if it is not inside it.
        else:
            my_dic[ch] = 1
    # Find the maximum value inside the dictionary.
    max_value = max(my_dic.values())
    
    # Make a loop to find the key correlated to maximum 
    # value of the dictionary.
    for key, value in my_dic.items():
        if value == max_value:
            # Display the key and value that belong to
            # highest repeatation inside the loop.
            print(key, value)

if __name__ == '__main__':
    main()       
            


