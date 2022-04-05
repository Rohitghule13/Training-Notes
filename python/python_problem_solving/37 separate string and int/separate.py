string_Num = input("Enter Input Here : ").split()
num = []
string = []
for i in range(len(string_Num)):
    if string_Num[i].isnumeric():
        num.append(string_Num[i])
    else:
        string.append(string_Num[i])
print(num)
print(string)