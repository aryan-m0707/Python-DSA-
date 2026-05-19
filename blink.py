n = 'gasgg54@#vsc$#sd!s*'
count = 0
copy = ""

for i in n:
    if(ord(i)>=65 and ord(i)<90):
        count += 0
    elif(ord(i)>=97 and ord(i)<122):
        count += 0
    elif(ord(i)>=48 and ord(i)<57):
        count += 0
    else:
        count+=1
    
print(count)