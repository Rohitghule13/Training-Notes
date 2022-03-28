class integertostring:
    def convert(self,a):
        self.a = str(a)
        print("string ",self.a)

try:
   integer = int(input("Enter the number : "))
   obj = integertostring()
   obj.convert(integer)
except BaseException:
    print("somthing went wrong please enter the number ")