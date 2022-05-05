# doubly Linkedlist

class node:  # node class for assign the node to heap of the memory

    def __init__(self, data):  # constructor to create data,next pointer and previous pointer
        self.data = data
        self.next_pointer = None  # next pointer used for pointing the next node
        self.prev_pointer = None  # previous pointer used for pointing the pprevious node
    

class Linkedlist:  # create Linkedlist class in it create several method to create link
    def __init__(self):
        self.head = None  # head var for storing first node
        self.last_node = None  # last_node for storing last node
        
    # function is for add node at last in the link list 
    def addAtTail(self, a):
        if self.head == None:
            self.head = node(a)
            self.next_pointer = None
            self.prev_pointer = None
            return True

        elif self.head.next_pointer == None:
            new_node = node(a)
            self.head.next_pointer = new_node
            new_node.prev_pointer = self.head
            new_node.next_pointer = None
            self.last_node = new_node
            return True
        else:
            # temp = self.head
            # while(temp.next_pointer!=None):
            #     temp = temp.next_pointer
            # new_node = node(a)
            # temp.next_pointer = new_node
            # new_node.prev_pointer = temp
            # new_node.next_pointer = None
            # last_node = new_node
            temp = self.last_node
            new_node = node(a)
            self.last_node = new_node
            self.last_node.prev_pointer = temp
            temp.next_pointer = self.last_node
            return 0
            
    # function for add node in front of the link list 
    def add_At_Head(self, a):

        temp = self.head
        self.head = node(a)
        self.head.next_pointer = temp
        temp.prev_pointer = self.head
        return
    # search ELement and return the node 
    def search_Element(self,a):
        if self.head==None:
            print("Linked list is Empty!")
            return False
        elif(self.head.data==a):
            return self.head
        elif(self.last_node.data==a):
            return self.last_node
        else:
            temp = self.head
            while(temp!=None):
                if temp.data == a:
                    return temp
                temp = temp.next_pointer
            print("Element is not present in Linked list ")
            return False
            
    # delete Node HEre 
    def delete_Node(self,a):
        if self.head==None:
            print("Linked list is Empty!")
            return False
        else:
            temp = self.search_Element(a)
            if temp:
                if temp.next_pointer==None:
                    prev = temp.prev_pointer
                    prev.next_pointer = None 
                    self.last_node = prev
                
                else:
                    prev = temp.prev_pointer
                    nextt = temp.next_pointer
                    prev.next_pointer = nextt 
                    nextt.prev_pointer = nextt 
                    del temp
                    print("Deleted Node Succussecfully!")
            else:
                print("NOde is not present in linked list")
                return False
                
    # display function for print the list in console 
    def display(self):     # display linked list node data 
        if self.head == None:  # when head pointer is none follow if 
            print("Linked List is Empty !")
            return False    # if head pointer point to the none return false 
        else:
            temp = self.head
            while (temp != None):   # repeat loop until temp pointer has point to the none 
                print(temp.data, end="->")   # display node data 
                temp = temp.next_pointer   # move temp pointer to the next node 
            print("None")
            return
    
    # display function for display list in reverse order in console 
    def Display_End_First(self):   # this function used for display node data in reverse order

        print("From End To First ")
        if self.head == None:       # check link list is empty if it is so follow the function
            print("Linkedlist is Empty !")
            return False
        temp = self.last_node     #  temparary pointer to point last node in list 
        while (temp != None):    # repeat loop until temp has none
            print(temp.data, end="->")   # display node data 
            temp = temp.prev_pointer    # move temp pointer to the previous node 
        print("None") 
        return True


llist = Linkedlist()
llist.addAtTail(4)

llist.addAtTail(2)
llist.addAtTail(1)

llist.display()
print(llist.head.data)
print(llist.head.next_pointer.prev_pointer.data)

llist.add_At_Head(0)
llist.display()
print(llist.last_node.data)
llist.Display_End_First()
llist.delete_Node(1)
llist.display()
print(llist.last_node.data)
llist.delete_Node(2)
llist.display()
temp = llist.search_Element(0)
print(temp)
print(llist.last_node.data)
llist.delete_Node(11)

# llist.delete_Node()
