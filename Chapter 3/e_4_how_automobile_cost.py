# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:17:16 2022

@author: Ali

Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
"""

def main():
    loan_paymanet = int(input("Please enter the monthly cost for loan payment: "))
    insurance = int(input("Please enter the monthly cost for insurance: "))
    gas = int(input("Please enter the monthly cost for gas: "))
    oil = int(input("Please enter the monthly cost for oil: "))
    tires = int(input("Please enter the monthly cost for tires: "))
    maintenance = int(input("Please enter the monthly cost for maintenance: "))
    
    total_month_cost(loan_paymanet, insurance, gas, oil, tires, maintenance)
    total_annual_cost(loan_paymanet, insurance, gas, oil, tires, maintenance)
    
def total_month_cost(loan_paymanet, insurance, gas, oil, tires, maintenance):
    total_mon_cost = loan_paymanet + insurance + gas + oil + maintenance
    print("The total monthly cost is", format(total_mon_cost, ',.0f'))
    
def total_annual_cost(loan_paymanet, insurance, gas, oil, tires, maintenance):
    total_ann_cost = (loan_paymanet + insurance + gas + oil + maintenance) * 12
    print("The total annual cost is", format(total_ann_cost, ',.0f'))
    
main()