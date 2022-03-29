try:
    string1 = input("Enter the string1 : ")
    string2 = input("Enter the string2 : ")
    if(len(string1)==len(string2)):
        print("True")
    else:
        print("False")
except BaseException:
    print("somthing went wrong please check")