class Queue:
    qu = []
    def enQueue(self,a):
        self.qu.append(a)
        return 

    def deQueue(self):
        return self.qu.pop(0)
    
    def displayQueue(self):
        print(self.qu)

Qu = Queue()
for i in range(1,5):
    Qu.enQueue(i)
Qu.displayQueue()
Qu.deQueue()
Qu.displayQueue()
print("DeQueue one front element from Queue :-",Qu.deQueue())
print("Avilable Queue :-",end=' ')
Qu.displayQueue()
