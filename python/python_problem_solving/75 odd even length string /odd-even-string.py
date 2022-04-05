string = input("Enter string : ").split()
for i in range(len(string)):
    if len(string[i])%2!=0:
        st = (string[i].replace(""," ")).split()
        st = reversed(st)
        st = "".join(st)
        print(st,end=" ")
    else:
        print(string[i],end=" ")