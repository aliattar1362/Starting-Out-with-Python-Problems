def main():
    annual_profit = 23/100 # Annual profit in percentage(23%)

    # The projected amount of sales is asked here
    total_sales = int(input("Enter the projected amount of total sales: "))

    # Profit is multipication of annual profit at amount of total sales
    profit = total_sales * annual_profit

    # Print the profit of company
    print(format(profit, ',.0f'))

main()