class Stack:     #stack class 
    stack = []   # stack list for adding element

    def push(self,val):    # push method adding element into the stack
        self.stack.append(val)
        return 

    def pop(self):         # retrive element from the stack
        return self.stack.pop()
    
    def Top(self):         # showing top element in stack
        print(self.stack[-1])
        return 
    
    def Display_stack(self): # Display whole stack
        print(self.stack)

obj = Stack()
# adding element into the stack each element added on the top of the stack
obj.push(1)
obj.push(2)
obj.push(3)

# Display Top element in stack
obj.Top()

# get top element from the stack
obj.pop()

# Disaplay whole stack
obj.Display_stack()

    