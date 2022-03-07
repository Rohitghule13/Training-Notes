#this program on Employee detail
class Person:
    _address = ""
    _phone = 000000000
    _email = ""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def contact_detail(self,add,phone_number,email):
        self._address = add
        self._phone = phone_number
        self._email = email
    def Display_personal(self):
        print(f"Name : {self.name}\nAge : {self.age}\nContact Detail : {self._address}\n{self._email}\n{self._phone}")
class Employee(Person):
    def __init__(self,name,age):
        self.name = name
        super().__init__(name,age)
    def Insert_Employee_detail(self,position,salary,bank_acc):
        self.postion = position
        self.salary = salary
        self.bank_acc = bank_acc
    def Display_Employee_detail(self):
        print(f"Name : {self.name}\nAge : {self.age}\nposition : {self.postion}")
rohit = Employee("rohit ghule",24)
rohit.Insert_Employee_detail("software Engineer",320000,65484553254)
add = "Ghule washi Tq.washi Dist.osmanabad maharashtra 413503"
email = "rohitghule131@gmail.com"
number = 8766778688
rohit.contact_detail(add,email,number)
rohit.Display_personal()
rohit.Display_Employee_detail()
