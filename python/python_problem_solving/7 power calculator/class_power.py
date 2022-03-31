class power:
    def claculate_power(self,a,b):
        print("result : ",a**b)

try:
    obj = power()
    a = int(input("Enter the number : "))
    b = int(input("Enter the power : "))
    obj.claculate_power(a,b)
except BaseException:
    print("somthing went wrong please enter the number in integer ")