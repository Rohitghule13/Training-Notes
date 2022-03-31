def find_duplicate(lis):
    origin = sorted(list(set(lis)))
    dup = []
    for i in range(len(origin)):
        if lis.count(origin[i])>1:
            dup.append(origin[i])
    print("duplicate element List : ",dup)
lis = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1, 12,88,7,6,2]
find_duplicate(lis)
