'''Factorial Solution'''
def factorial(num):  #num = 1
    if num <= 1:     #base condition
        return 1
    return num * factorial(num - 1)

#4*factorial(3)
# 3*factorial(2)
# 2*factorial(1)
# 4*3*2*`= 24`