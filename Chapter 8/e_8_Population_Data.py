# This program reads the file’s contents into a list. 
# The program should display the following data:
# • The average annual change in population during 
# the time period.
# • The year with the greatest increase in 
# population during the time period.
# • The year with the smallest increase in 
# population during the time period .

def make_list_fucn():
    # Open the file in read mode.
    infile = open("USPopulation.txt", "r")
    
    # Make an empty list.
    my_list = []
    
    # Use loop to add informations of line's content
    # inside the list.
    for line in infile:
        line = line.rstrip('\n')
        line = int(line)
        my_list.append(line)
    infile.close()   
    return my_list

#################################################################
def make_annual_change_list(main_list):
    # make an empty list to keep the data
    # regarding annual change of population.
    ann_ch_list = []
    
    # Initialize index to read the values of
    # items inside the population list.
    index = 0
    
    # Initialize counter to stop while loop
    # if reach to length of population list. 
    counter = 0
    
    # Define while loop to calculate the annual change
    # of population and put them inside a list.
    while not counter == len(main_list)-1:
        # Calculate the annual change of population
        # from each two consecutive values.
        annual_change = abs(main_list[index+1] -\
                main_list[index])
        
        # Make a list consits of annual change of 
        # population.
        ann_ch_list.append(annual_change)
        
        # Raise the values of couner and index
        # for next process.
        counter += 1
        index += 1
    # Return the list of annual change of population.
    return ann_ch_list

#################################################################   
def ave_calculator(main_list):
    # Initialize total value for sum of values in 
    # annual population increase.
    total = 0
    
    # For loop to calculate the sum of yearly 
    # population change base on list. 
    for value in main_list:
        total += value
    
    # Calculate the average of yearly
    # population change. 
    ave = total/len(main_list)
    # Display the averange of yearly
    # population change.
    print("The average of yearly population change ",\
           "is ", format(ave, ',.0f'), ".", sep='')
    return ave
#################################################################



def main():
    
    my_list = make_list_fucn()  
    ann_ch_list = make_annual_change_list(my_list)
    ave_calculator(ann_ch_list)
    
    # Find the year with greatest increase
    # in population during the time period.
    greatest_increase_value = max(ann_ch_list)
    greatest_increase_index = ann_ch_list.index(greatest_increase_value)
    greatest_increase_year = (1950 + 1) + greatest_increase_index
    # Display the value of greatest population increase
    # and its year.
    print("The greatest population increase happend ",\
        "in ", greatest_increase_year,\
            " with the value of ",\
                format(greatest_increase_value, ',.0f'),\
                    ".", sep = '')
    
    # Find the year with  smallest increase increase
    # in population during the time period.
    smallest_increase_value = min(ann_ch_list)
    smallest_increase_index = ann_ch_list.index(smallest_increase_value)
    smallest_increase_year = (1950 + 1) + smallest_increase_index
    # Display the value of smallest population increase
    # and its year.
    print("The smallest population increase happend ",\
        "in ", smallest_increase_year,\
            " with the value of ",\
                format(smallest_increase_value, ',.0f'),\
                    ".", sep = '')
        
# Call the main function.
if __name__ == "__main__":
    main()