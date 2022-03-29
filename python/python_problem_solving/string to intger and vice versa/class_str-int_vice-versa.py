class viceversa:
    def convert(self,st):
        print("this is in integer number : ",int(st))
        print("this is in string number : ",str(st))
        return 

try:
    st = input("Enter the 0 - 9 in integer format : ")
    obj = viceversa()
    obj.convert(st)
except BaseException:
    print("somthing went wrong please Enter the number 0-9 to perform vice versa opration")
