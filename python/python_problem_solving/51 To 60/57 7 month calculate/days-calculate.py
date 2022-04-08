from datetime import date # get date from datetime module

def calculate_month(datee):  # function for calculating 

    seven_month = date(2022,7,1)
    D = seven_month-datee
    return abs(D.days) # return days
    
try: # try is for track and handle error in code 

    day = int(input("Enter Day : "))      # getting day from console input
    month = int(input("Enter Month : "))  # getting month from console input
    year = int(input("Enter Year : "))    # getting year from console input
    datee = date(year,month,day)
    print(f"From 2022/1/1 To {year}/{month}/{day}:  ",calculate_month(datee),"Days") # call funtion and calculte days
    
except BaseException as E: # exception for handlling error

    print("Somthing went wrong Please enter date in number only error : ",E)