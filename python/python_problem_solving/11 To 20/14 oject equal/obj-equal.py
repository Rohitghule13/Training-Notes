str1 = "123"
str2 = "12"
# outer if check similar type of object and length
if(type(str1)==type(str2) and len(str1)==len(str2)):
    if(str1 == str2):
        print("Type of object, length, and property are same !")
    else:
        print("Type of object, lenght are same but property is not same !")
elif(type(str1)==type(str2)):
    if(str1 == str2):
        print("Type of object and property are same, but length is not same !")
    else:
        print("Type of object same but property and length is not same !")
else:
    print("object, length and property aren't same ! ")
