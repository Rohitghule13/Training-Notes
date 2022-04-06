def character(string1,string2):
    if len(string1)==len(string2):
        return True
    return False
string1 = input("Enter string1 : ")
string2 = input("Enter string2 : ")
print(character(string1,string2))