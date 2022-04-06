class addition:
    def sum_of_two_number(self,a,b):
        print("result is : ",a+b)

try:
   a = int(input("enter the first number : "))
   b = int(input("enter the second number : "))
   obj = addition()
   obj.sum_of_two_number(a,b)

except BaseException:
    print("somthing went wrong please enter the integer number only")