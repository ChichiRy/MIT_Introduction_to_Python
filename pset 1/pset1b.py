# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:21:39 2022

@author: user
"""
# Program computes number of months required to raise a down payment for a dream home, given a semi-annual salary raise over the period, down_payment
# of 25% of the total cost, and an interest rate of 4% per annum.

#Takes user inputs; annual salary, %monthly salary saved, cost of dream home.
annual_salary = float(input("Enter your annual salary: "));
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "));
total_cost = float(input("Enter the cost of your dream home: "));
semi_annual_raise = float(input("Enter the semi-annual-raise, as a decimal: "));

#Assignment of some important varaiables
portion_down_payment = 0.25 * total_cost;
current_savings = 0;
r = 0.04;
months = 0

#Main function loop calculating number of months
while (current_savings < portion_down_payment):
    monthly_salary = annual_salary / 12
    current_savings *= (1 + (r / 12));
    current_savings += (portion_saved * monthly_salary);
    months += 1;
    if (months % 6 == 0):
        annual_salary *= (1 + semi_annual_raise);

print("Number of months:", months)
