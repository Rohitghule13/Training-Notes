string = input("Enter string : ").split() # get string from console

for i in range(len(string)):   # check each string length and compare it is odd or even

    if len(string[i])%2!=0: # if length of string is divided by 2 and remain 0
        st = (string[i].replace(""," ")).split() # adding space in string character and split into array
        st = reversed(st)  # reversed array
        st = "".join(st) # join array char and make it as string 
        print(st,end=" ") # print reversed string

    else: # else is follwed when length of string is even
        
        print(string[i],end=" ")