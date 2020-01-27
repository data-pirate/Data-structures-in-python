class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def printqueue(self):
        for each in self.items:
            print(each)



# make object of the queue class
q = queue()

# adding values to the queue

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print('on insertion !')
q.printqueue() # will print the entire queue

print('=======================') # just for an additional space between insertion and deletion !

# deleting something form the queue
q.dequeue()
q.dequeue()

print('after deletion !')
q.printqueue()