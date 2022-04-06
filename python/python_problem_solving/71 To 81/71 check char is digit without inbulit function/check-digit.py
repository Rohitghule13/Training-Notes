digit = ['0','1','2','3','4','5','6','7','8','9']
char = input("Enter the string : ")
statement = False
for i in char:
    if i in digit:
        print(i,"This char is digit ")
        statement = True
if statement:
    print("in string, there have char digit ")
else:
    print("in string, char digit is not there ")
