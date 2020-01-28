class stack:
    def __init__(self):
        self.items = list() # Empty list for stack

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        self.items.pop(0)

    def printstack(self):
        for each in self.items:
            print(each)


stk = stack() # object of class stack !

stk.push(10) # call method push() to add something to the stack 
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)
stk.push(60)

print('==============** On pushing to stack **====================')
stk.printstack()

print()

stk.pop()
stk.pop()
print('================** After Deletion **==================')

stk.printstack()
