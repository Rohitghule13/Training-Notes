def agedays(age):
    print("Days : ",age*336)

try:
    age = int(input("Enter the age : "))
    agedays(age)
except BaseException:
    print("Somthing went wrong please enter age in number ")
