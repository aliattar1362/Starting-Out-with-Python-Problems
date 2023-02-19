def main():
    
    text = 'Stop And Smell The Roses.'
    
    new_text = ''
    
    my_list = []
    
    for ch in text:
        ch = ch.lower()
        new_text += ch.lower()
        
    print(new_text)
    
    value = 0
    letter = ''
    
    
    for ch in new_text:
        my_list = new_text.split(ch)
        
        new_value = len(my_list) -1
        new_letter = ch
        
        if new_value > value:
            value = new_value
            letter = new_letter
    
    print('letter:', letter)
    print('value', value)

if __name__ == '__main__':
    main()       
            


