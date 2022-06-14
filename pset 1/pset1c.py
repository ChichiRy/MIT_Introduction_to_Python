# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:38:33 2022

@author: user
"""


#Takes user inputs; annual salary, %monthly salary saved, cost of dream home.
starting_salary = float(input("Enter your annual salary: "));

#Assignment of some important varaiables
semi_annual_raise = 0.07;
total_cost = 1000000;
portion_down_payment = 0.25 * total_cost;
current_savings = 0;
r = 0.04;
months = 0;
high = 10000;
low = 0;
epsilon = 100;
bisection_search = 0;
mid = (high + low) / 2;

#Main function loop calculating number of months
while (abs(current_savings - portion_down_payment) > epsilon):
    bisection_search += 1;
    current_savings = 0;
    months = 0;
    annual_salary = starting_salary;
    while (months < 36):
        monthly_salary = annual_salary / 12;
        current_savings *= (1 + (r / 12));
        current_savings += (mid / 10000 * monthly_salary);
        months += 1;
        if (months % 6 == 0):
            annual_salary *= (1 + semi_annual_raise);
    checker = mid;
    if(current_savings < portion_down_payment):
        low = mid;
        mid = (high + low) / 2;
    elif(current_savings > portion_down_payment):
        high = mid;
        mid = (high + low) / 2;
    if(checker == mid):
        break

if(mid == checker):
    print("It is not possible to pay the down payment in three years.");
else:
    print("Best savings rate:", (int(mid) / 10000));
    print("Steps in bisection search: {}".format(bisection_search))