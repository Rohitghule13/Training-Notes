def lcm(num1,num2):
    largest = 0
    if num1>num2:
        largest = num1
    else:
        largest = num2
    while(True):
        if(largest%num1==0)and(largest%num2==0):
            print(f"{largest} this is LCM of {num1}, {num2}")
            break
        largest += 1
    print()
num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))
lcm(num1,num2)