lis = [a for a in range(1,21)]
print("odd sqaured number : ",end="")
for i in lis:
    if i%2!=0:
        a = lambda a : a*a
        print(i,":",a(i),end=" | ")
print()