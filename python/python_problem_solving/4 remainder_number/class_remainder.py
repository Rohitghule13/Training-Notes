class remainder:
    def remainder_of_number(self,a,b):
        print(a%b)
    
try :
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    obj = remainder()
    obj.remainder_of_number(a,b)
except BaseException:
    print("somthing went wrong please number only ")