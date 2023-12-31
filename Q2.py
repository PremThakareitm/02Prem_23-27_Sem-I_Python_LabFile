# 2.1 Write a program that define the list of defines the list of define countries that are in BRICS.


# countries = ['BRAZIL', 'RUSSIA', 'INDIA', 'CHINA', 'SOUTH AFRICA']
# ans = input("Enter the country:").upper()

# if ans in countries:
#     print(ans, "is in BRICS")
# else:
#     print(ans, "is not in BRICS")

# print("\nBRICS Countries:")
# for country in countries:
#     print(country)



# 2.2 Write a program to traverse a list in reverse order.
# 1.By using Reverse method.
# 2.By using slicing

# l = [1, 2, 3, 4, 5]
# print("\nOriginal List:",l)
# reversed_list = list(l)
# reversed_list.reverse()

# print("Reversed List using reverse method:", reversed_list)

# l2 = [1, 2, 3, 4, 5]
# print("\nOriginal List:",l2)
# reversed_list_slice = l2[::-1]

# print("Reversed List using slicing:", reversed_list_slice)


# 2.3 Write a program that scans the email address and forms a tuple of username
# and domain.

# def username(email):

#     username, domain = email.split("@")
#     email = (username, domain)
#     return email

# email_address = input("Enter your email address: ")
# result = username(email_address)
# print("Username:", result[0])
# print("Domain:", result[1])


# 2.4 Write a program to create a list of tuples from given list having number and
# add its cube in tuple.
# i/p: c= [2,3,4,5,6,7,8,9]

# c = [2, 3, 4, 5, 6, 7, 8, 9]

# result = [(num, num ** 3) for num in c]

# print("List of Tuples (Number, Cube):", result)


# 2.5 Write a program to compare two dictionaries in Python?
# (By using == operator)

d1 = {'a': 2, 'b': "Prem", 'c': "Thakare"}
d2 = {'a': 2, 'b': "Prem", 'c': "Thakare"}

if d1 == d2:
    print("The dictionaries are Same.")
else:
    print("The dictionaries are not Same.")


# 2.6 Write a program that creates dictionary of cube of odd numbers in the range.

start = int(input("Enter the Start of range:"))
end = int(input("Enter the End of range:"))

odd_cubes= {num: num**3 for num in range(start, end + 1) if num % 2 != 0}
print("Dictionary of Cubes of Odd Numbers:", odd_cubes)


# 2.7 Write a program for various list slicing operation.
a= [10,20,30,40,50,60,70,80,90,100]
# i. Print Complete list

print("Complete List:", a)

# ii. Print 4th element of list

print("4th Element:", a[3])

# iii. Print list from0th to 4th index.

print("List from 0th to 4th index:", a[0:5])

# iv. Print list -7th to 3rd element

print("List from -7th to 3rd element:", a[-7:3])

# v. Appending an element to list.

a.append(101)
print("List after Appending 101:", a)

# vi. Sorting the element of list.

a.sort()
print("Sorted List:", a)

# vii. Popping an element.

popped_element = a.pop()
print("Popped Element:", popped_element)
print("List after Popping:", a)

# viii. Removing Specified element.

a.remove(60)
print("List after Removing 60:", a)

# ix. Inserting an element at a specified index
a.insert(2, 35)
print("List after Inserting 35 at index 2:", a)

# x. Counting the occurrence of a specified element
count_30 = a.count(30)
print("Count of 30 in the List:", count_30)

# xi. Extending list
extension_list = [120, 130, 140]
a.extend(extension_list)
print("List after Extending:", a)

# xii. Reversing the list
a.reverse()
print("Reversed List:", a)