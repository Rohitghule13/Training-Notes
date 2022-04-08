sub_list = int(input("Enter no of sub list : "))
dup = [0 for i in range(sub_list)]
for i in range(sub_list):
    index = int(input(f"Enter Index from 1 To {sub_list} : "))
    dup.pop(index-1)
    dup.insert(index-1,list(map(int,input("Enter List : ").split())))

print(dup)