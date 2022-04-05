from datetime import date
try:
    year = int(input("Enter the year : "))
    month = int(input("Enter the Month : "))
    Date = date(year,month,13)
    if Date.strftime("%A")=="Friday":
        print(F"there is Friday in this Date {Date}")
    else:
        print(F"there is not Friday in this Date {Date}")
except BaseException as e:
    print("somthing went wrong enter month and year in 'integer' : ",e)