class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous Node Does Not Exist in the Linked List')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

lst = LinkedList()
lst.append('A')
lst.append('B')
lst.prepend('C')
lst.insert_after_node(lst.head, 'D')
lst.printlist()
