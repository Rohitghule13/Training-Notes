class string:
    def getstring(self):
        self.st = input("Enter the any string : ")
        return
    def printstring(self):
        print("string : ",self.st.upper())
        return

S = string()
S.getstring()
S.printstring()