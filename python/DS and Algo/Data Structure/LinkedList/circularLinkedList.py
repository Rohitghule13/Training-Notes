class node:
    def __init__(self,data):
        self.data = data 
        self.nextt = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addAtTail(self,val):
        temp = self.head
        if(temp==None):
            self.head = node(val)
            self.head.nextt = self.head
            return
        else:
            while(True):
                # temp = temp.nextt
                if temp.nextt==self.head:
                    break
                temp = temp.nextt
            point = node(val)
            point.nextt = self.head
            temp.nextt = point 
            return
    
    def display(self):

        if self.head==None:
            print("there are no element in list!")
            return

        temp = self.head
        print(temp.data,end="->")
        temp = temp.nextt

        while(True):
            print(temp.data,end="->")
            if(temp.nextt==self.head):
                break
            temp = temp.nextt
        print("Circular Mode")
    
    def addAtHead(self,val):
        temp = self.head
        while(True):
                # temp = temp.nextt
                if temp.nextt==self.head:
                    break
                temp = temp.nextt
        first = self.head
        self.head = node(val)
        self.head.nextt = first
        temp.nextt = self.head
        return

llist = Linkedlist()
llist.addAtTail(2)
llist.addAtTail(1)
temp = llist.head
llist.display()
llist.addAtHead(5)
llist.display()