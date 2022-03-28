class ageToString:
    def age_to_days(self,age):
        print("Days ",age*336)

try :
    age = int(input("Enter the number : "))
    obj = ageToString()
    obj.age_to_days(age)
except BaseException:
    print("somthing went wrong please enter the age in number ")