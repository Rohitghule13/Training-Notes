from audioop import reverse


tup = (1,2,3,4,5)
print("Orignal tuple : ",tup)
tup = reversed(list(tup))
tup = tuple(tup)
print("After reverse : ",tup)
