tup = (1,2,3,4)
#Tuple is immutable datastructure it can not modify 
#So we need to convert tuple to list then change can be possible after
#change covert list into tuple 
tup = list(tup)
tup.append(5)
tup.append(6)
tup = tuple(tup)
print("Tuple : ",tup)