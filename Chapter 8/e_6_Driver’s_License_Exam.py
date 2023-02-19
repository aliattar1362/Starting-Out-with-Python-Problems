# This program stores the correct answers in a list. 
# The program reads the student’s answers for each of 
# the 20 questions from a text file and store the answers in
# another list. (Create your own text file to test the 
# application.) After the student’s answers have been read 
# from the file, the program should display a message 
# indicating whether the student passed or failed the exam. 
# (A student must correctly answer 15 of the 20 questions
# to pass the exam.) It should then display the total number 
# of correctly answered questions, the total number of 
# incorrectly answered questions, and a list showing the 
# question numbers of the incorrectly answered questions.

def main():
    # Create the key_list for the correct answers.
    key_list = ['B', 'D', 'A', 'A', 'C', 'A', 'B','A', 'C', 'D',
                'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    
    # Create student answer list.
    stu_ans_list = ['A', 'D', 'A', 'A', 'C', 'A', 'B','A', 'C', 'D',
                'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'C']
    
    # Initalize an empty list to keep the index 
    # of wrong answers.
    wrong_index_list = []
    
    # Initialize the counter to calculate the amount of correct 
    # answers in student's list.
    counter = 0
    # Initialize the index for items of both lists.
    index = 0
    
    # Make a loop to check the accuracy of the student's answers.
    while index != len(key_list):
        # If the answer is mathced with key list.
        if key_list[index] == stu_ans_list[index]:
            # Increase the counter.
            counter += 1
        else:
            # Because index was started form 1
            # raise the index with 1.
            w_index = index+1
            wrong_index_list.append(w_index)
            
        # Raise the index to check next item.
        index += 1
        
    # Display the total number of corrects answers.  
    print(f"The number of correct answers is {counter}.")
    
    # Display the total number of wrong answers. 
    wrong_ans = len(key_list) - counter
    print(f"The number of correct answers is {wrong_ans}.")
    
    # Display the list of indices containg wrong answers.
    print("The list of incorrect answers is:", wrong_index_list)
    
# Call the main function.
if __name__ == "__main__":
    main()
            
        
        