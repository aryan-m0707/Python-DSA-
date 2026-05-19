stringSent = input("Enter original string: ")
stringRec = input("Enter received string: ")

for ch in stringSent:
    if ch not in stringRec:
        print("Missing character is:", ch)
        break
    else:
        stringRec = stringRec.replace(ch, "", 1)