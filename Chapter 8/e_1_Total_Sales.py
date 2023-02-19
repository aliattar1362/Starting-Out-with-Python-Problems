# This program asks the user to enter a store’s 
# sales for each day of the week. The amounts are 
# stored in a list. The loop is used to calculate the 
# total sales for the week and the result is displayed.

def main():
    # Global variable for days of week.
    Week_days = 7
    
    # Make an empty list to keep the daily sales.
    sales_list = []
    
    # Initialize total sales.
    total = 0
    
    # Prompt the user to enter the store’s 
    # sales for each day of the week.
    for day in range(Week_days):
        # Ask the daily sale.
        print("Enter the store's sales for", day+1, end='')
        daily_sale = int(input("#: "))
        # Add the sale for this day to list.
        sales_list.append(daily_sale)
        # Update the total value of sale.
        total += daily_sale
        
    # Display the total amount of week sale.
    print("The total amount of this week's sales is ",\
          total, '.', sep='')
        
# Call the main function.
if __name__ == "__main__":
    main()
    