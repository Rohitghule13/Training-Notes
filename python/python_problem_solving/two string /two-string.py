def string():
    string1 = input("Enter first string : ")
    string2 = input("Enter second string : ")
    if len(string1)==len(string2):
        print(string1)
        print(string2)
    elif len(string1)>len(string2):
        print(string1)
    else:
        print(string2)
    return 
string()