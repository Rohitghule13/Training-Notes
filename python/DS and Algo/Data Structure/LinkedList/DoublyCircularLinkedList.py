# doubly Circular LinkedList
class node:
    def __init__(self,data):
        self.data = data
        self.next_pointer = None
        self.prev_pointer = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_Node = None
    
    def add_At_Tail(self,a):
        if self.head == None:
            self.head = node(a)
            self.head.next_pointer = self.head
            self.head.prev_pointer = self.head
            self.last_Node = self.head
            return
        else:
            temp = self.head
            if temp.next_pointer == self.head:
                new_node = node(a)
                self.head.next_pointer = new_node
                new_node.prev_pointer = self.head
                new_node.next_pointer = self.head
                self.last_Node = new_node
                return
            else:
                temp = self.last_Node
                new_node = node(a)
                temp.next_pointer = new_node
                new_node.next_pointer = self.head
                new_node.prev_pointer = temp
                self.last_Node = new_node 
                return 
            
    def display_List(self):
        if self.head == None:
            print("Linked List is empty!")
            return
        else:
            temp = self.head
            while(True):
                print(temp.data,end="->")
                temp = temp.next_pointer
                if temp == self.head:
                    break
            print("Circular Mode")

llist = LinkedList()
llist.add_At_Tail(4)
llist.add_At_Tail(3)
llist.add_At_Tail(2)
llist.display_List()
llist.add_At_Tail(1)
llist.display_List()
