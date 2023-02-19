# Write a program that creates a dictionary containing course 
# numbers and the room numbers of the rooms where the courses meet. 
# The dictionary should have the following keyvalue pairs:
    
#   Course Number (key)    Room Number (value)
#   CS101                  3004
#   CS102                  4501
#   CS103                  6755
#   NT110                  1244
#   CM241                  1411

# The program should also create a dictionary containing course 
# numbers and the names of the instructors that teach each
# course. The dictionary should have the following key-value pairs:

# Course Number (key)   Instructor (value)
# CS101                 Haynes
# CS102                 Alvarado
# CS103                 Rich
# NT110                 Burke
# CM241                 Lee

# The program should also create a dictionary containing course 
# numbers and the meeting times of each course. The dictionary 
# should have the following key-value pairs:
    
# Course Number (key)   Meeting Time (value)
# CS101                 8:00 a.m.
# CS102                 9:00 a.m.
# CS103                 10:00 a.m.
# NT110                 11:00 a.m.
# CM241                 1:00 p.m.

def main():
    my_dic = {'CS101':[3004,'Haynes', '8:00 a.m.'], 
              'CS102':[4501,'Alvarado', '9:00 a.m.'],
              'CS103':[6755,'Rich', '10:00 a.m.'],
              'NT110':[1244,'Burke', '11:00 a.m.'],
              'CM241':[1411,'Lee', '1:00 p.m.']}
    
    course_number = input('Enter the course number: ')
    
    for key, value in my_dic.items():
        if key == course_number:
            print(value[0])
            print(value[1])
            print(value[2])
        
if __name__ == "__main__":
    main()
    