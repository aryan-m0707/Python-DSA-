import math
input=[79,77,54,81,48,34,25,16]

count =0
for i in range(len(input)):
    value = input[i]
    root = math.isqrt(value)
    if root*root == value:
        count+=1

print(count)