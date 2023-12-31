# 5.1 Write a program to create my_module for addition of two numbers and import
# it in main script.

import my_module

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
result = my_module.addition(num1, num2)

print("Result of addition:", result)
