# 1.8 Write a program to print the following pattern

# i)
# *
# * *
# * * *
# * * * *
# * * * * *

# a=int(input("Enter the number of rows:"))
# for i in range(0,a+1):
#     for j in range (0,i):
#         print("*",end=" ")
#     print("\n")



# ii)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# a = int(input("Enter the number of rows: "))
# for i in range(1, a+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# iii)
# *
# * * *
# * * * * *
# * * * * * * *
# * * * * * * * * *

# a = int(input("Enter the number of rows: "))
# for i in range(1, a+1):
#     for j in range(2*i-1):
#         print("*", end=" ")
#     print()
