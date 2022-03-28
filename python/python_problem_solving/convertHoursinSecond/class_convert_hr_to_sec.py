class HourstoSecond:
    def convert_hours_to_second(self,x):
        self.minutes = x*60
        self.second = self.minutes*60
        print("Seconds ",self.second)
try:
    x= int(input("enter hours "))
    sec = HourstoSecond()
    sec.convert_hours_to_second(x)
except BaseException:
    print("somthing went wrong please enter hours only in number")
    