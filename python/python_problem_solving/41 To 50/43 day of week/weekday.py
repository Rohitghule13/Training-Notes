import datetime 
try:
    Day = int(input("Enter date in number : "))
    Month = int(input("Enter Month in number : "))
    Year = int(input("Enter Year in number : "))
    x = datetime.datetime(Year,Month,Day)
    print("Week day is : ",x.strftime("%A"))
except BaseException as e:
    print("somthing went wrong please enter number in integer : ",e)