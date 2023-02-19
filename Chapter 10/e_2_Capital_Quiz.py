# Write a program that creates a dictionary
# containing the U.S. states as keys and their
# capitals as values. (Use the Internet to get a
# list of the states and their capitals.) The
# program should then randomly quiz the user
# by displaying the name of a state and asking
# the user to enter that state’s capital.
# The program should keep a count of the number
# of correct and incorrect responses. 
#(As an alternative to the U.S. states, 
#the program can use the names of
# countries and their capitals.)

def main():
    my_dic = {'Netherlands':'Amsterdam', 
              'Andorra':'Andorra',
              'Greece':'Athens',
              'Serbia':'Belgrade',
              'Germany':'Berlin',
              'Switzerland':'Bern',
              'Slovakia':'Bratislava',
              'Belgium':'Brussels',
              'Romania':'Bucharest',
              'Hungary':'Budapest',
              'Moldova':'Chisinau',
              }
    
    counter = 0
    
    for num in range(3):
        country, capital = my_dic.popitem()
        your_answer = input('Guess the capital' \
              f' city for {country}: ')
        
        if your_answer == capital:
            print('Your reply was correct.'\
                  ' Congratulations!')
            counter += 1
            
    print('In Total you answer correctly', end = '')
    print(f' to {counter} questions!', end = '')
    print(f' Also, you missed {3-counter} ', end = '')
    print('question.')
          
        
if __name__ == "__main__":
    main()
    