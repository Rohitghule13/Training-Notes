# Circular Linkedlist
class node:  # create node to heap of memory 
    def __init__(self,data):
        self.data = data  # data variable 
        self.nextt = None  # next pointer 

class Linkedlist: # linked list class 
    def __init__(self):
        self.head = None  # head pointer point to the first node

    def addAtTail(self,val):  # add element to the last function 

        temp = self.head  # create temp varaible to store 
        if(temp==None):  # check if first head node is none 
            self.head = node(val) # if true so assgin node to the first 
            self.head.nextt = self.head
            return
        else:
            while(True): # if gets false so find the last node in the list 
                # temp = temp.nextt
                if temp.nextt==self.head: # if temp is return point to the head
                    break    # so break the loop
                temp = temp.nextt  

            point = node(val)   
            point.nextt = self.head
            temp.nextt = point 
            return

    # place node to the front of list 
    def addAtHead(self,val):  
        temp = self.head   # create temp variable 
        while(True):  # get last node 
                # temp = temp.nextt
                if temp.nextt==self.head:
                    break
                temp = temp.nextt

        first = self.head # get previous first node 
        self.head = node(val) # create first node 
        self.head.nextt = first # assign the previous node as a second node 
        temp.nextt = self.head  # assign last node next pointer point to the first node
        return

    # search element function
    def search_Element(self,a):

        if self.head == None:   # check first element is equal to none 
            print("Linked list is Empty!")
            return False

        temp = self.head
        while(temp!=None): # iterate loop until temp is not None
            if temp.data == a: # if temp data is equal to the a var 
                return temp    # return temp object 

            temp = temp.nextt
            if temp == self.head:  # if temp is equal to head
                break # break the loop
                
        print("element is not present in Linked list")
        return False
    
    # delete node function
    def delete_Element(self,a):
       
        if self.head == None:
            print("Linked List is Empty!")
            return False
        
        elif(self.search_Element(a)==False):
            return False
    
        else:
            temp = self.head
            prev = self.head
            while(temp!=None):
                if temp.data==a:
                    break
                prev = temp
                temp = temp.nextt
                if temp == self.head:
                    return False
                        
            if temp.nextt==None:
                prev.nextt = self.head
                del temp
            else:
                prev.nextt = temp.nextt
                del temp 
    # display function         
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
    
    

llist = Linkedlist()
llist.addAtTail(2)
llist.addAtTail(1)
temp = llist.head
llist.display()
llist.addAtHead(5)
llist.display()
llist.search_Element(0)
llist.delete_Element(1)
llist.display()

