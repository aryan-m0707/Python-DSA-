ab = [-1,2,4,3,2,5,5]

bc = []

ab = bc
count = 0

for i in ab:
    for j in bc:
        if ab[i] == bc[j]:
            count += 1
    
print (count)