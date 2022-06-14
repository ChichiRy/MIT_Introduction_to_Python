# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:50:51 2022

@author: user
"""
# Program computes number of months required to raise a down payment for a dream home, given constant salary over the period, down_payment
# of 25% of the total cost, and an interest rate of 4% per annum.

#Takes user inputs; annual salary, %monthly salary saved, cost of dream home.
annual_salary = float(input("Enter your annual salary: "));
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "));
total_cost = float(input("Enter the cost of your dream home: "));

#Assignment of some important varaiables
portion_down_payment = 0.25 * total_cost;
current_savings = 0;
r = 0.04;
monthly_salary = annual_salary / 12
months = 0

#Main function loop calculating number of months
while (current_savings < portion_down_payment):
    current_savings *= (1 + (r / 12));
    current_savings += (portion_saved * monthly_salary);
    months += 1;

print("Number of months:", months)
