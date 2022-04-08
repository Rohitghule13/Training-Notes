digit = ['0','1','2','3','4','5','6','7','8','9'] # list used for reference for checking 
                                                 # digit present in string 
char = input("Enter the string : ")      # get input from console 

statement = False            # if digit in string statement is true

for i in char:           # checking string character 
    if i in digit:
        print(i,"This char is digit ")
        statement = True
if statement:  # if digit is present in string statement is true if cond. is followed
    print("in string, there have char digit ")
else:                # else is followed when statement is false
    print("in string, char digit is not there ")
