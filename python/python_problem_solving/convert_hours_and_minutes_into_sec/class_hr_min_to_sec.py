class convert:
    def hour_minute_to_sec(self,hour,minute):
        minute = (hour*60)+minute
        second = minute*60
        print("Second : ",second)
try :
    obj = convert()
    hour,minute = map(int,input("Enter the number : ").split(maxsplit=1))
    obj.hour_minute_to_sec(hour,minute)
except BaseException:
    print("somthing went wrong please enter the number in integer")