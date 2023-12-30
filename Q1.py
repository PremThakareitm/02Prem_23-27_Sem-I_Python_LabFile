# 1.1 Write a program to compute Simple Interest.
# 1.2 Write a program to perform arithmetic, Relational operators.
# 1.3 Write a program to find whether a given no is even &amp; odd.
# 1.4 Write a program to print first n natural number &amp; their sum.
# 1.5 Write a program to determine whether the character entered is a Vowel or not
# 1.6 Write a program to find whether given number is an Armstrong Number.
# 1.7 Write a program using for loop to calculate factorial of a No.
# 1.8 Write a program to print the following pattern


# p=float(input("Enter the Principal Amount :"))
# r=float(input("Enter the Rate of Rate :"))
# t=float(input("Enter the time period (yrs):"))

# si=(p*r*t)/100

# print("Simple Intrest:",si)
# print("Total Amount:",si+p)

# def arithmetic_relational(a, b):
#     equal = a == b
#     not_equal = a != b
#     greater = a > b
#     less = a < b
#     greater_less = a >= b
#     less_greater = a <= b
    
#     print(f"Arithmetic Operations:")
#     print(f"{a} + {b} = {a+b}")
#     print(f"{a} - {b} = {a-b}")
#     print(f"{a} * {b} = {a*b}")
#     print(f"{a} / {b} = {a/b}")
#     print(f"{a} % {b} = {a%b}")
#     print(f"{a} ** {b} = {a**b}")
    
#     print("\nRelational Operations:")
#     print(f"{a} == {b} : {equal}")
#     print(f"{a} != {b} : {not_equal}")
#     print(f"{a} > {b} : {greater}")
#     print(f"{a} < {b} : {less}")
#     print(f"{a} >= {b} : {greater_less}")
#     print(f"{a} <= {b} : {less_greater}")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# arithmetic_relational(num1, num2)

# def check(num):
#     if num % 2 == 0:
#         print(f"{num} is an even number.")
#     else:
#         print(f"{num} is an odd number.")

# a = int(input("Enter a number: "))
# check(a)


# def prime_no(n):
#     sum=0
#     l=[]
#     for i in range(1, n+1):
#             l.append(i)
#             sum += i
#     print(f"First {n} natural numbers: {l}")
    
#     print(f"Sum of the first {n} natural numbers: {sum}")

# num = int(input("Enter the value of n: "))
# prime_no(num)

# def vowel(char):
#     vowels = "aeiouAEIOU"
#     if char in vowels:
#         return True
#     else:
#         return False

# str = input("Enter a character: ")

# if len(str) == 1 and str.isalpha():
#     if vowel(str):
#         print(f"{str} is a vowel.")
#     else:
#         print(f"{str} is not a vowel.")
# else:
#     print("Please enter a single alphabetical character.")

# def armstrong_no(num):

#     num_str = str(num)
#     num_digits = len(num_str)

#     armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
#     return armstrong_sum == num

# numo = int(input("Enter a number: "))

# if armstrong_no(numo):
#     print(f"{numo} is an Armstrong number.")
# else:
#     print(f"{numo} is not an Armstrong number.")

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         factorial_s = 1
#         for i in range(1, n + 1):
#             factorial_s *= i
#         return factorial_s

# num = int(input("Enter a number: "))
# result = factorial(num)

# if type(result) == int:
#     print(f"The factorial of {num} is {result}.")
# else:
#     print(result)


