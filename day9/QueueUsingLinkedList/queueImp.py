class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
class Queue:
    def __init__(self):
        self.LinkedList=LinkedList()
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False
    
    def enQueue(self,val):
        node=Node(val)
        if self.isEmpty():
            self.LinkedList.head=node
            self.LinkedList.tail=node
        else:
            self.LinkedList.tail.next=node
            self.LinkedList.tail=node
    
    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty.')
        else:
            revnode=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            print('Removed element is:',revnode)
    
    def peek(self):
        if self.isEmpty():
            print('Queue is Empty.')
        else:
            print('Peek element is:',self.LinkedList.head.value)
        
    def display(self):
        if self.isEmpty():
            print('Queue is Empty.')
        else:
            print('Displaying Queue.')
            temp=self.LinkedList.head
            while temp is not None:
                print(temp.value,end=' ')
                temp=temp.next
            print()

obj=Queue()
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
obj.enQueue(5)
obj.display()
obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.display()
obj.peek()


