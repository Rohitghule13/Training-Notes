class remainder:
    def remainder_of_number(self,a,b):
        print(a%b) # module for getting remainder 
    
try :
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    obj = remainder() # object is created

    obj.remainder_of_number(a,b) # caling method 

except BaseException:
    print("somthing went wrong please number only ")