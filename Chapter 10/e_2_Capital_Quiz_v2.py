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

import random

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
    
    new_list = list(my_dic.keys())
    random.shuffle(new_list)
    
    # initialize an acculumator for correct answers.
    range_counter = 0
    ans_counter = 0
    
    for country in new_list:
        if range_counter != 3: 
            
            your_answer = input('Guess the capital' \
                      f' city for {country}: ')
                
            # Get the index of coutry.   
            #index =  new_list.index(country)    
            #print('index:', index)
            #print('my_dic[country]:', my_dic[country])
            #print('new_list[index]:', new_list[index])
            #print('your_answer:', your_answer)
            
            if your_answer == my_dic[country]:
                print('Your reply was correct.'\
                          ' Congratulations!')
                ans_counter += 1
                
            range_counter += 1
            
    print(ans_counter)
                
if __name__ == "__main__":
    main()
    