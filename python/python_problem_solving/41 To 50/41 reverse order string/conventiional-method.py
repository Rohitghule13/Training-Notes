st = input("Enter string here : ")
for i in range(len(st)-1,-1,-1):
    print(st[i],end="")
print()
st = st.split()
st.reverse()
print(" ".join(st))