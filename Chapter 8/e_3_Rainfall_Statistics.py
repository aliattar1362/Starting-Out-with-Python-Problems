# This program asks the user enter the total rainfall for 
# each of 12 months into a list. The program should calculate 
# and display the total rainfall for the year, the average 
# monthly rainfall, and the months with the highest and 
# lowest amounts.

def main():
    # Global variable for months of year.
    year_months = 12
    
    # Make an empty list to keep the monthly rainfall.
    rainfall_list = []
    
    # Initialize total rainfall.
    total = 0
    
    for month in range(year_months):
        print("Enter the amount of rainfall for ",\
              month+1, sep="", end ="")
        rainfall_amount = int(input("# month: "))
        rainfall_list.append(rainfall_amount)
        total += rainfall_amount
        
    # Calculate the average of monthly rainfall.
    ave = total/year_months
    # Display the average of monthly rainfall.
    print("The average of monthly rainfall is ",\
          format(ave,'0.2f'), ".", sep="")
        
    # Find and display the month with highest rainfall.
    highest_rainfall_amount = max(rainfall_list)
    highest_rainfall_index = rainfall_list.index(highest_rainfall_amount)
    print("The highest rainfall belongs to month ",\
          highest_rainfall_index, " with amount of ",\
              highest_rainfall_amount, ".", sep="")
        
    # Find and display the month with lowest rainfall.
    lowest_rainfall_amount = min(rainfall_list)
    lowest_rainfall_index = rainfall_list.index(lowest_rainfall_amount)
    print("The lowest rainfall belongs to month ",\
          lowest_rainfall_index, " with amount of ",\
              lowest_rainfall_amount, ".", sep="") 
        
# Call the main function.
if __name__ == "__main__":
    main()
        
    