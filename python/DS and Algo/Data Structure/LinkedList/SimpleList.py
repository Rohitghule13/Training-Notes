class node:
    
    def __init__(self,data):
        self.data = data
        self.nextt = None

class Linkedlist:

    head = None

    def addAtTail(self,val):
        if self.head==None:
            self.head = node(val)
            return True
        else:
            temp = self.head
            while temp.nextt!=None:
                temp = temp.nextt
            a = node(val)
            temp.nextt = a 
            a.nextt = None
            return True
    
    def addAtHead(self,val):
        temp = self.head
        self.head = node(val)
        self.head.nextt = temp
        return True
    

    def displayList(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp = temp.nextt
        print("None")
    
    def searchElement(self,val):
        temp = self.head
        place = 1
        while(temp!=None):
            if temp.data==val:
                
                return True,place
            place += 1
            temp = temp.nextt
        return False
    
    def deleteElement(self,val):
        temp = self.head
        prev = self.head
        while(temp!=None):
            if temp.data==val:
                break
            prev = temp
            temp = temp.nextt
        if temp.nextt==None:
            prev.nextt = None
            del temp
            return True
        nexttt = temp.nextt
        prev.nextt = nexttt
        del temp
        return True

llist = Linkedlist()
# llist.addAtTail(0)
# llist.addAtTail(5)
for i in range(7):
    llist.addAtTail(i)
llist.addAtHead(7)
llist.displayList()
print(llist.searchElement(6))
llist.deleteElement(3)
llist.displayList()
llist.deleteElement(6)
llist.displayList()