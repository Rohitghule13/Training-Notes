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
        # place = 1
        while(temp!=None):
            if temp.data==val:
                return temp
            # place += 1
            temp = temp.nextt
        print("Element is not present in list")
        return False
    
    def deleteElement(self,val):
        if(self.searchElement(val)==False):
            print("Element is not present in list")
            return
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
    
    def inseration_in(self,i,j):
        if self.head == None:
            print("Linked list is Empty")
            return False
        else:
            temp = self.searchElement(i)
            new_node = node(j)
            new_node.nextt = temp.nextt
            temp.nextt = new_node
            
            return
    
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
llist.searchElement(11)
llist.deleteElement(11)
llist.inseration_in(1,11)
llist.displayList()
llist.inseration_in(4,6)
llist.displayList()
i = llist.searchElement(11)
print(i.data,i.nextt)


