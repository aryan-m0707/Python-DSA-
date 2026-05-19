# def hello():
#     print("Hello World")

# hello()
# hello()

# it's posible to return multiple value in python 

# def arithmatic():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum, sub, div, mul
# # print(arithmatic())
# ans=arithmatic()
# print("Arithmatic= ",ans)

# -----------------------------------------------------------------------------

#how many types of argument we pass in function ?
# 1.positional argument
# 2.keyword arg
# 3.default arg
# 4.variable length arg/variable no. of arg

# 1.positional argument
# def arithmatic(a,b):
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum, sub, div, mul
# ans=arithmatic(5,5)
# print("Arithmatic= ",ans)

# 2.keyword arg
# def credential(username, password):
#     if username == password:
#         print("Login successefully")
#     else:
#         print("invalid credential")

# credential(username="Admin",password="Admin") # key word name and parameter name must be same


# 3.default arg
# def cityname(city="Pune"):
#     print(city)

# cityname("Nagpur")
# cityname("Mumbai")
# cityname("")
# cityname()#if default argument is not set then function gives error


# 4.variable length arg/variable no. of arg
# def cityname(*name):
#     print(name)
# cityname("Nagpur","Mumbai","Pune","Delhi")

# ----------------------------------------------------------------------------------------------------

# modularity approch in function
# import sys

# def add():
#     a=int(input("Enter value for A: "))
#     b=int(input("Enter value for B: "))
#     print(a+b)

# def sub():
#     a=int(input("Enter value for A: "))
#     b=int(input("Enter value for B: "))
#     print(a-b)

# def div():
#     a=int(input("Enter value for A: "))
#     b=int(input("Enter value for B: "))
#     print(a/b)

# def mul():
#     a=int(input("Enter value for A: "))
#     b=int(input("Enter value for B: "))
#     print(a*b)

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Division")
#     print("4. Multiplication")
#     print("5. Exit")

#     choice=int(input("Enter your choice: "))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         div()
#     elif choice == 4:
#         mul()
#     elif choice == 5:
#         sys.exit()
    
