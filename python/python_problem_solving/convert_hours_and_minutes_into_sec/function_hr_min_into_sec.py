def hour_min_sec(hour,minute):
    minute = (hour*60)+minute
    second = minute*60
    print("Second : ",second)
try:
    hour,minutes = map(int,input("Enter the number : ").split(maxsplit=1))
    hour_min_sec(hour,minutes)
except BaseException:
    print("somthing went wrong please enter number in integer")