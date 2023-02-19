# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:55:12 2022

@author: Ali

Modularizing with Functions
Hal owns a business named Make Your Own Music, which sells guitars, drums, banjos,
synthesizers, and many other musical instruments. Hal’s sales staff works strictly on commission. At the end of the month, each salesperson’s commission is calculated according to
Table 6-1.
Table 6-1 Sales commission rates
Sales This          Month Commission Rate
Less than $10,000   10%
$10,000–14,999      12%
$15,000–17,999      14%
$18,000–21,999      16%
$22,000 or more     18%
For example, a salesperson with $16,000 in monthly sales will earn a 14 percent
 commission ($2,240). Another salesperson with $18,000 in monthly sales will
 earn a 16 percent commission ($2,880). A person with $30,000 in sales will earn
 an 18 percent commission ($5,400).
Because the staff gets paid once per month, Hal allows each employee to
 take up to $2,000 per month in advance. When sales commissions are calculated, 
 the amount of each employee’s advanced pay is subtracted from the commission. 
 If any salesperson’s commissions are less than the amount of their advance, 
 they must reimburse Hal for the difference. To calculate a salesperson’s monthly pay, 
 Hal uses the following formula:
pay=sales*commission rate-advanced pay
Hal has asked you to write a program that makes this calculation for him. The following
general algorithm outlines the steps the program must take.
1. Get the salesperson’s monthly sales.
2. Get the amount of advanced pay.
3. Use the amount of monthly sales to determine the commission rate.
4. Calculate the salesperson’s pay using the formula previously shown. If the amount is
negative, indicate that the salesperson must reimburse the company.
"""

# This program is generated to simulate the tossing of a coin. 
# Define the main function.
def main():
    # Get the salesperson’s monthly sales.
    month_sales = float(input('Enter the monthly sales: '))
    # Get the amount of advanced pay.
    adv_pay = float(input('Enter the amount of advanced pay: '))
    # Call the commission calculator function. 
    comm_rate = commission_rate_func(month_sales)
    # Call the pay calculator function. 
    pay = pay_func(month_sales, comm_rate, adv_pay)
    # Call the display function to represent the monthly payment. 
    display_func(pay)
  
# This function determines the commission rate based on the monthly sales. 
def commission_rate_func(month_sales):
    if month_sales < 10000:
        comm_rate = 0.1 # Commission rate = 10%
    elif month_sales >= 10000 and month_sales < 14999:
        comm_rate = 0.12 # Commission rate = 12%
    elif month_sales >= 15000 and month_sales < 17999:
        comm_rate = 0.14 # Commission rate = 14%
    elif month_sales >= 18000 and month_sales < 21999:
        comm_rate = 0.16 # Commission rate = 16%
    else:
        comm_rate = 0.18 # Commission rate = 18%
    return comm_rate

# This function determines the the salesperson’s pay to each staff. 
def pay_func(month_sales, comm_rate, adv_pay):
    pay = month_sales * comm_rate - adv_pay
    return pay
# This function displays the payment amount to the staff.
def display_func(pay):
    if pay < 0:
        print('The salesperson must reimburse the company $', end='' )
        print(format(abs(pay),',.2f'),'!', sep='')
    else:
        print('The salesperson will get $', format(pay, ',.2f'), sep='')
        
           
# Call the main function.    
main()


