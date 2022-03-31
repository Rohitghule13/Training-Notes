def check_five(st):
    if st.count("5")>1:
        return False
    return True
try:
    start = int(input("Enter the start : "))
    finish = int(input("Enter the finish : "))
    five = ["55","555","5555","55555"]
    for i in range(start,finish):
        if i%7==0 and check_five(str(i)):
            print(i,end=",")
except BaseException:
    print("somthing went wrong please enter number in integer")

