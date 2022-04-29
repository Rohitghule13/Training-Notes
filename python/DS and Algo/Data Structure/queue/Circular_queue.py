# define the Queue class 
class Queue:
    def __init__(self,size): # define the important flags and variable 
        self.size = size                      # get the size of queue
        self.qu = [None for i in range(size)] # generete empty list here 
        self.front = self.rear = -1           #this is front and rear flags
    
    def enQueue(self,val):   # method to add the element in queue
        
        if self.rear == -1:  # check weather the queue is initial empty 
            self.rear = 0    # set the rear flag on 0
            self.front = 0   # also set the front flag on 0
            self.qu[self.rear] = val  # add element where rear flag on

        elif (self.rear+1) % self.size == self.front: # checking the queue is full or not using condition
            # like rear is 2 size is 3 and front is 0 it means no dequeue opereation is performed it means 
            # queue space is getting occupied by element like (2+1)%3==0 condition gets true and 
            # method return false 

            print("Queue is Full")
            return False

        else: # above two condition gets fails follow this

            self.rear = (self.rear+1) % self.size # perform math function and get the rear value
            self.qu[self.rear] = val             # add elemet in queue wherever on rear flag in queue
            # print(self.rear)

    def deQueue(self): # this method is used for dequeue element from queue

        if self.front == None: # condition check queue is empty or not
            print("Queue is Empty")
            self.front = -1    # set front flag

        else: # above condition gets false follow this

            temp = self.qu[self.front] # retrive element from queue
            self.qu[self.front] = None  # when element gets retrive once on that place palce None
            self.front = (self.front + 1 )% self.size # set the front value by perform math function
            print("Queue Element :- ",temp)  

    def displayQueue(self): # display queue method
        if self.front==-1:
            print("The Queue is Empty")
        else:
            print("Orignal Queue :- ",self.qu)
            print("front to rear :- ",self.qu[self.front:])

q = Queue(3)
q.displayQueue()
q.enQueue(2)
q.enQueue(1)
q.enQueue(3)
q.enQueue(4)
q.displayQueue()
q.deQueue()
q.displayQueue()
q.enQueue(4)
q.displayQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()