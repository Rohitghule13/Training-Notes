#small number in list
def small(lis):
    sm = lis[0]
    for i in range(len(lis)):
        if sm>lis[i]:
            sm = lis[i]
    return sm 

#large number in list

def high(lis):
    sm = lis[0]
    for i in range(len(lis)):
        if sm<lis[i]:
            sm = lis[i]
    return sm 

lis = [1, 3, 5, 7, 10]
missing_num = []
start = small(lis)
finish = high(lis)

#find out missing number 
for i in range(start,finish):
    if i in lis:
        continue
    missing_num.append(i)

#summing all missing number 
summ = 0
for i in missing_num:
    summ += i

print("Missing number sum : ",summ)