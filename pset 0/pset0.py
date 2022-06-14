# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:56:48 2022

@author: user
"""
#Program to compute x to a particular number, and log of x to base 2.

import math

num1 = int(input("Enter a number x: "));
num2 = int(input("Enter a number y: "));

print("X ** Y =", (num1**num2));
print("log(x) =", math.log(num1, 2));
