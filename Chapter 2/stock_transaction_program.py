"""
    This program will calculate the financial summary of Joe's
    trading in stock market in last month.
"""


def main():
    # The number of shares that Joe purchased
    purchased_shares = 1000
    # Paid money to purchase shares, per share
    paid_money = 32.87
    # The amount of paid commission to stockbroker in percent for buying
    paid_commission_buying = 0.02
    # The number of shares that was sold 
    sold_shares = 1000
    # Obtained money after selling shares, per share
    obtained_money = 33.92
    # The amount of paid commission to stockbroker in percent for sellinf
    paid_commission_selling = 0.02
    # Calculate the amount of money Joe paid for the stock.
    paid_for_stock = purchased_shares * paid_money 
    print('The paid money to buy the shares:', format(paid_for_stock,',.0f'),'$')
    # Calculate the amount of commission Joe paid his broker when he bought the stock.
    paid_for_commission_buying = purchased_shares * paid_money * paid_commission_buying
    print('The paid commission to buy the shares:', format(paid_for_commission_buying,',.0f'),'$')
    # Calculate the amount that Joe sold the stock for.
    sold_stock = sold_shares * obtained_money 
    print('The obtained money for selling the shares:', format(sold_stock,',.0f'),'$')
    # Calculate the amount of commission Joe paid his broker when he sold the stock.
    paid_for_commission_selling = sold_shares * obtained_money * paid_commission_selling
    print('The paid commission for selling the shares:', format(paid_for_commission_selling,',.0f'),'$')
    # Calculate the net profit of Joe's trade
    net_profit = sold_stock - paid_for_stock - paid_for_commission_buying - paid_for_commission_selling
    print('The net profit of Joe\'s trade:', format(net_profit,',.0f'),'$')
main()
