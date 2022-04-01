tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
lis = list(tuple1)
for i in range(len(tuple1)):
    for j in range(len(tuple1)-1):
        if (lis[j][1]>lis[j+1][1]):
            temp = lis[j]
            lis[j] = lis[j+1]
            lis[j+1] = temp
tuple1 = tuple(lis)
print(tuple1)