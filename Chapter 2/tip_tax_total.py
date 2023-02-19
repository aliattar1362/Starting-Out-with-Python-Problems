def main():
    # Ask the charge for the food: c_f
    charge_food = int(input("Enter the charge for food: "))
    # Calculate the 15% tip
    tip = charge_food * 0.15
    # Calculate 7% sales tax: s_t
    sales_tax = charge_food * 0.07
    # Calculate total expenses:
    total_expenses = charge_food + tip + sales_tax
    # Display each of upper amounts
    print("The amount of tip is", format(tip, ",.0f"))
    print("The amount of sales_tax is", format(sales_tax, ",.0f"))
    print("The amount of total_expenses is", format(total_expenses, ",.0f"))
main()  