#this is python program file
# function program
def get_add(x,y):#function is created using def keyword

    return x + y # return the value

z = get_add(5,5) # calling function passing parameter

print(z)        # display the result

# writing classes
class Vehical:
    def __init__(self,manu,oil,mileage):
        self.manu = manu
        self.oil = oil
        self.mileage = mileage
    def print_detail(self):
        print("manufacuring by : ",self.manu)
        print("petrol/disel : ",self.oil)
        print("mileage of Vehical : ",self.mileage)

bike = Vehical("honda","petrol",62)
bike.print_detail()

#control statement
count = 0
while True:
    count += 1
    print(count,end=' ')
    if count==5:
        break    #break the loop when count=5
name = "this is for code"
for i in name:
    if i=='i': #ignore i char
        continue #it jump to the next
    print(i,end="")
