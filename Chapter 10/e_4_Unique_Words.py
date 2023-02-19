# Write a program that opens a specified text
# file and then displays a list of all the unique
# words found in the file.
# Hint: Store each word as an element of a set

def main():
    my_text = '''After this statement executes, the 
    mysetvariable will reference an empty set. 
    You can also pass one argument to the setfunction. 
    The argument that you pass must be an object that
    contains iterable elements, such as a list, a tuple,
    or a string.'''
    my_list = my_text.split(' ')
    
    my_set = set()
    
    for item in my_list:
        if item not in my_set:
            my_set.add(item)
    
    print(my_set)
  
main()
    