# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))


# def capitalizeFirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))


# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))


# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))


# def reverse(string):
#     if len(string)<=1:
#         return string
#     return string[len(string)-1]+reverse(string[0:len(string)-1])

# print(reverse('python'))
# print(reverse('appmillers'))
# print(reverse(''))


# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num+recursiveRange(num-1)
# print(recursiveRange(6))
# print(recursiveRange(7))


# def isPalindrom(str):
#     if len(str) == 0:
#         return True
#     if str[0] != str[len(str)-1]:
#         return False
#     return isPalindrom(str[1:-1])
# print(isPalindrom('awesome'))
# print(isPalindrom('foobar'))
# print(isPalindrom('tacocat'))
# print(isPalindrom('amanaplanacanal'))
# print(isPalindrom('awesome'))


def someRecursive(arr,cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:],cb)
    return True
def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True
print(someRecursive([1,2,3,4],isOdd))
print(someRecursive([4,6,8,9],isOdd))
print(someRecursive([4,8,6],isOdd))