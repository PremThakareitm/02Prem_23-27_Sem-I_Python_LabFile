# 3.1 Write a program to extend a list in python by using given approach.
# i. By using + operator.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print("Extended List using + operator:", list3)

# ii. By using Append ()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print("Extended List using append():", list1)

# iii. By using extend ()

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print("Extended List using extend():", list1)


# 3.2 Write a program to add two matrices.

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

print("Matrix after Addition:")
for row in result_matrix:
    print(row)


# 3.3 Write a Python function that takes a list and returns a new list with distinct
# elements from the first list.

def display_distinct_elements(input_list):
    return list(set(input_list))

# Example
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
distinct_list = display_distinct_elements(original_list)
print("Original List:", original_list)
print("List with Distinct Elements:", distinct_list)


# 3.4 Write a program to Check whether a number is perfect or not.

def perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

num=int(input("Enter a number:"))
if perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")


# 3.5 Write a Python function that accepts a string and counts the number of upper-
# and lower-case letters.
# string_test= &#39;Today is My Best Day&#39

def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string_test = 'Today is My Best Day'
print(string_test)
upper, lower = count(string_test)
print(f"Number of Upper-case letters: {upper}")
print(f"Number of Lower-case letters: {lower}")


