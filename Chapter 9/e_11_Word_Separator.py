def main():
    
    text = 'StopAndSmellTheRoses.'

    # Create an empty list.
    my_list = []

    # Initialize the counter for order of letters in text.
    letter = 0

    while letter < len(text):
        letter = 0
        word = ''
        
        for ch in text:
            if ch.isupper() and letter == 0:
                word += ch
                
            elif ch.isupper():
                break
            
            else:
                word += ch
            
            letter += 1
            
        my_list.append(word)
        text = text[letter : ]
        
    for item in my_list[ : -1]:
        print(item, end='')
        print(' ', end='')
        
    print(my_list[-1])
            
if __name__ == '__main__':
    main()       
            


