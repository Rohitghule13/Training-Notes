try:
    hour,minutes = map(int,input("Enter the hour and minutes ").split(maxsplit=1))
    minutes = (hour*60)+minutes
    second = minutes*60
    print("seconds ",second)
except BaseException:
    print("somthing went wrong please enter number in integer ")