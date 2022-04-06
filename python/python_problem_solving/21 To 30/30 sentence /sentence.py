st = input("Enter the sentence : ")
upper = 0
lower = 0
digit = 0
letter = 0
for i in range(len(st)):
    if st[i].isalpha():
        letter += 1
        if st[i].islower():
            lower += 1 
        else:
            upper += 1 
    elif st[i].isdigit():
        digit += 1 
print("Number of Letters : ",letter)
print("Number of Digit : ",digit)
print("Number of Lower : ",lower)
print("Number of Upper : ",upper)