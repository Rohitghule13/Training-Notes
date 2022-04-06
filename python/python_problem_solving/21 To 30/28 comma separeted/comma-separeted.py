try:
    string = input("enter string : ")
    string = (string[0:string.index(" ")].replace(',',' ')).split()
    string.sort()
    print(",".join(string))
except BaseException:
    print("somthing went wrong please check it once")
