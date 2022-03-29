class number:
    def Next_number(self,x):
        print("Number : ",x)
        x += 1
        print("Next Number : ",x)
        return 

x = int(input("Enter the Number : "))
obj = number()
obj.Next_number(x)