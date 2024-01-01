# 4.1 Write a program to Create Employee Class &amp; add methods to get employee
# details &amp; print.

# class Employee:
#     def __init__(self, name, employee_id, department):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department

#     def details(self):
#         return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nDepartment: {self.department}"

# employee1 = Employee("Prem Thakare", "02", "Btech")
# print(employee1.details())


# 4.2 Write a program to take input as name, email &amp; age from user using
# combination of keywords argument and positional arguments (*args
# and**kwargs) using function,

# def details(*args, **kwargs):
#     name = input("Enter Name: ")
#     email = input("Enter Email: ")
#     age = int(input("Enter Age: "))

#     print("Additional Details:")
#     for arg in args:
#         print(arg)
    
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# details("Additional Arg1", "Additional Arg2", additional_kwarg="Additional KWarg")


# 4.3 Write a program to admit the students in the different
# Departments(pgdm/btech) and count the students. (Class, Object and Constructor).

# class ITM:
#     count = 0
#     def get(self):
#         self.name = input("Enter the name of the student: ")
#         self.age = int(input("Enter the age: "))
#         self.dep = int(input("Enter the department (1 for B.Tech, 2 for PGDM): "))
#         ITM.count += 1

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         if self.dep == 1:
#             print("Department: B.Tech")
#         elif self.dep == 2:
#             print("Department: PGDM")
#         print()


# students = int(input("Enter the number of students: "))

# btech_students = []
# pgdm_students = []

# for i in range(students):
#     student = ITM()
#     student.get()
    
#     if student.dep == 1:
#         btech_students.append(student)
#     elif student.dep == 2:
#         pgdm_students.append(student)

# print("\nB.Tech Students:")
# for student in btech_students:
#     student.display()

# print("\nPGDM Students:")
# for student in pgdm_students:
#     student.display()

# print("\nTotal Admissions:", ITM.count)


# 4.4 Write a program that has a class store which keeps the record of code and
# price of product display the menu of all product and prompt to enter the quantity of
# each item required and finally generate the bill and display the total amount.

# class Store:
#     def __init__(self):
#         self.products = {"Product1": 10, "Product2": 20, "Product3": 30}
#         self.bill = {}

#     def display_menu(self):
#         print("Product Menu:")
#         for product, price in self.products.items():
#             print(f"{product}: Rs.{price}")

#     def generate_bill(self):
#         print("Your Bill:")
#         total_amount = 0
#         for product, quantity in self.bill.items():
#             price = self.products[product]
#             total_price = price * quantity
#             print(f"{product} x {quantity}: Rs.{total_price}")
#             total_amount += total_price
#         print("Total Amount: Rs.{}".format(total_amount))

#     def take_order(self, product, quantity):
#         if product in self.products and quantity > 0:
#             self.bill[product] = quantity
#             print(f"{quantity} {product}(s) added to your bill.")
#         else:
#             print("Invalid product or quantity.")

# store = Store()
# store.display_menu()
# store.take_order("Product1", 2)
# store.take_order("Product3", 1)
# store.generate_bill()


# 4.5 Write a program to take input from user for addition of two numbers using
# (single inheritance).

# class Addition:
#     def add_numbers(self, num1, num2):
#         return num1 + num2

# class UserInput(Addition):
#     def get_user_input(self):
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         result = self.add_numbers(num1, num2)
#         print(f"The sum of {num1} and {num2} is: {result}")


# user_input = UserInput()
# user_input.get_user_input()


# 4.6 Write a program to create two base classes LU and ITM and one derived class.
# (Multiple inheritance).

# class LU:
#     def display_LU(self):
#         print("LU Class")

# class ITM:
#     def display_ITM(self):
#         print("ITM Class")

# class Derived(LU, ITM):
#     pass


# derived_object = Derived()
# derived_object.display_LU()
# derived_object.display_ITM()


# 4.7 Write a program to implement Multilevel inheritance,
# GrandfatherFather-Child to show property inheritance from grandfather to
# child.

# class Grandfather:
#     def __init__(self):
#         self.gfname = " Thakare"
#         self.inheritance = 70000000

# class Father(Grandfather):
#     def __init__(self):
#         super(Father, self).__init__()
#         self.fname = input("Enter the Father Name: ") + self.gfname
#         self.finheritance = float(input("Enter the Property purchased by Father: ")) + self.inheritance

# class Child(Father):
#     def __init__(self):
#         super(Child, self).__init__()
#         self.child = input("Enter the Child Name: ") + " " + self.fname
#         self.cinheritance = float(input("Enter the Property purchased by " + self.child + " is: ")) + self.finheritance

# c = Child()
# print("\nHi,", c.child)
# print("\nYour Total Assets is:\nInherited:", c.inheritance, "\nPurchased:", c.finheritance, "\nYour Property:", c.cinheritance)


# 4.8 Write a program Design the Library catalogue system using inheritance take
# base class (library item) and derived class (Book, DVD &amp; Journal) Each derived
# class should have unique attribute and methods and system should support Check
# in and check out the system. (Using Inheritance and Method overriding)

# class LibraryItem:
#     def __init__(self, title, item_id, no_copies):
#         self.title = title
#         self.item_id = item_id
#         self.no_copies = no_copies
#     def display(self):
#         print("\nTitle: ",self.title)
#         print("Item ID: ",self.item_id)
#         print("Num Copies: ",self.no_copies)
#     def checkout(self):
#         cho=input("Enter the item ID:")
#         if (cho=="B12"):
#             ch=int(input("Enter the No of Copies: "))
#             if (ch<=self.no_copies):
#                 self.no_copies-=1
#             else:
#                 print("Insufficient Copies")
        

# class Book(LibraryItem):
#     def __init__(self, title, item_id, no_copies):
#         super().__init__(title, item_id, no_copies)
#         self.title = title
#     def display(self):
#         super().display()

# class DVD(LibraryItem):
#     def __init__(self, title, item_id, no_copies):
#         super().__init__(title, item_id, no_copies)
#         self.title = title
#     def display(self):
#         super().display()


# class Journal(LibraryItem):
#     def __init__(self, title, item_id, no_copies):
#         super().__init__(title, item_id, no_copies)
#         self.titler = title
#     def display(self):
#         super().display()



# book = Book("C++ Obj.", "B12", 10)
# dvd = DVD("Animal", "D13", 5)
# journal = Journal("Indian Journal", "J14",15)

# book.display()
# dvd.display()
# journal.display()

