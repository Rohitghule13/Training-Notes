def find_duplicate(lis):
    lis1 = lis 
    dup = []
    for i in range(len(lis1)):
        for j in range(i+1,len(lis)):
            if ((lis1[i]==lis[j]) and (lis[j] not in dup)):
                dup.append(lis[i])
    print("duplicate element List : ",dup)
lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1, 12,88,7,6,2]
find_duplicate(lis)