# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 07:25:02 2022

@author: Ali

Suppose you have a certain amount of money in a savings account that earns compound
monthly interest and you want to calculate the amount that you will have after a specific
number of months. The formula is
F = P* (1 +i)**t
The terms in the formula are as follows:
• F is the future value of the account after the specified time period.
• P is the present value of the account.
• i is the monthly interest rate.
• t is the number of months.
Write a program that prompts the user to enter the account’s present value, monthly interest
rate, and number of months that the money will be left in the account. The program should
pass these values to a function that returns the future value of the account after the specified
number of months. The program should display the account’s future value.
"""
def main():
    account_value, month_int_rate, num_mon = input_func()
    f = future_value_func(account_value, month_int_rate, num_mon)
    print('The future value of the account is: $', format(f,',.2f'))
    
def input_func():
    account_value = float(input('Enter the account’s present value: '))
    month_int_rate = float(input('Enter the monthly interest rate: '))
    num_mon = int(input('Enter the number of months that the money will be left in the account: '))
    return account_value, month_int_rate, num_mon

def future_value_func(p, i, t):
    f = p*(1+i)**t
    return f
main()