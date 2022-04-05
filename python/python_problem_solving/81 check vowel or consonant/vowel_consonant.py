vowel = "aeiouAEIOU"
char = input("Enter Char only : ")
if(len(char)==1):
    if char in vowel:
        print(f"'{char}' This charecter is vowel")
    else:
        print(f"'{char}' This character is consonant")
else:
    print("Please Enter One Chareacter only!")