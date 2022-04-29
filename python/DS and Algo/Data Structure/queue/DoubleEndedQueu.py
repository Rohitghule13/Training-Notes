# In this type of queue inseration and removal opeartion can be done from both end
# front and rear
class Queue:
    def __init__(self, size):
        self.size = size
        self.qu = [None for i in range(size)]
        self.front = self.rear = -1
 
    def insertFromEnd(self,a):
        if (self.rear+1) == self.size and self.front == 0:
            print("Sorry cant insert from End! queue is full")
            return False
 
        elif self.front==self.rear==-1:
            self.front = self.rear = 0
            self.qu[self.rear] = a
            return True
 
        elif (self.size+1)==self.rear and self.front>0:
            for i in range(0,self.rear):
                self.qu[i] = self.qu[i+1]
            self.qu[self.rear] = a
            self.front -= 1
            return True
        else:
            self.rear += 1
            self.qu[self.rear] = a
            return True

    def deQueueFromEnd(self):
        if self.rear==self.front==-1:
            print("Dequeu From End! Queue is Empty")
            return False

        elif (self.rear==self.front)and(self.rear==self.front!=-1):
            temp = self.qu[self.front]
            self.qu[self.front] = None
            self.front=self.rear = -1
            return temp

        else:
            temp = self.qu[self.rear]
            self.qu[self.rear] = None
            self.rear -= 1
            return temp

    def insertFromFront(self,a):
        if (self.rear+1) % self.size == self.front:
            print('sorry cant insert From Front! Queue is full')
        elif self.front==self.rear==-1:
            self.rear = 0
            self.front = 0
            self.qu[self.front] = a
        elif self.front>0:
            self.front -= 1
            self.qu[self.front] = a
            return True
        else:
            for i in range(self.rear,self.front-1,-1):
                self.qu[i+1] = self.qu[i]
            self.rear += 1
            self.qu[self.front] = a
            return True
    def deQueueFromFront(self):
        if self.front==self.rear==-1:
            print("Dequeue From Front side! Queue is Empty")
            return False

        elif (self.rear==self.front)and(self.rear==self.front!=-1):
            temp = self.qu[self.front]
            self.qu[self.front] = None
            self.front=self.rear = -1
            return temp
        
        else:
            temp = self.qu[self.front]
            self.qu[self.front] = None
            self.front += 1
            return temp

        
 
 
 
q = Queue(3)
q.insertFromEnd(4)
q.insertFromFront(3)
q.insertFromEnd(5)
q.insertFromFront(1)
print(q.qu)
print(q.deQueueFromFront())
print(q.deQueueFromEnd())
print(q.qu)
print(q.rear,q.front)
print(q.deQueueFromEnd())
print(q.qu)
print(q.rear,q.front)
q.insertFromFront(1)
print(q.qu)