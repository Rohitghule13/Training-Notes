def checkdivisible(a):

    if a%5==0:
        print(f"number of {a} is divisible 5")
    else:
        print(f"{a} can not divisible by 5")

try:
    a = int(input("Enter the number : "))
    checkdivisible(a)

except BaseException:
    print("enter the number in intger like 0 to 9")