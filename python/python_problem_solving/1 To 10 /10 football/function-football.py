class Footboll:
    def __init__(self):
        self.win = 0
        self.draw = 0
        self.loss = 0
    
    def Matches(self,a):
        print(f"Team played {a} matches")
        print("Wins : ",self.win)
        print("Draw : ", self.draw)
        print("Loss : ", self.loss)

    def points(self):
        point = (self.draw*10)+(self.win*20)
        print("Total points ",point)

try:
    matches = int(input("Enter Number Matchces played By Team : "))
    TeamA = Footboll()
    TeamA.win = int(input("ENter number of Wins : "))
    TeamA.draw = int(input("ENter number of draw : "))
    TeamA.loss = int(input("ENter number of loss : "))
    TeamA.Matches(matches)
    TeamA.points()
except BaseException as E:
    print("Somthing went Wrong Please Enter in integer only : ", E)