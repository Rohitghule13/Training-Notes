list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"] 
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        a = list1[i]+list2[j]
        list3.append(a)
print(list3)
