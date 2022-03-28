#first class 

class Myclass:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender
    def prininfo(self):
        print(f"your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"your gender is {self.gender}")

#child class 

class Employee(Myclass):
    def __init__(self, name, age, gender,position,salary):
        self.position = position
        self.salary = salary
        super().__init__(name, age, gender)
    def printemployeedetail(self):
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"gender : {self.gender}")
        print(f"position : {self.position}")
        print(f"salary : {self.salary}")
rohit = Employee("rohhit ghule",23,"male","software engineer",25000)
rohit.printemployeedetail()
rohit.prininfo()
