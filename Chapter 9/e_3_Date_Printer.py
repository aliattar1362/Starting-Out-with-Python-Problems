# This program reads a string from 
# the user containing a date in the form
# mm/dd/yyyy. It should print the date in
# the form March 12, 2012.

def main():
    # Get the date in requested format.
    print("Enter the date in this ", end="")
    date = input("format (mm/dd/yyyy): ")
    # Put the date inside the list.
    date = date.split('/')
    # Set the day from date list.
    day = date[1]
    # Set the month from date list.
    month = int(date[0])
    # Set the year from date list.
    year = date[2]
    
    # Define the condition to convert the
    # month number to its corresponded name.
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "Nobember"
    elif month == 12:
        month = "December"
        
    # Display the entire date according
    # to desired format.
    print(f"{month} {day}, {year}.")
        
# Call the main function    
if __name__ == "__main__":
    main()