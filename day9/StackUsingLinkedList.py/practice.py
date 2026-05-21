# Stack using linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    
    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        print('\n'.join(values))
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False 

    def push(self,val):
        node=Node(val)
        node.next=self.LinkedList.head
        self.LinkedList.head=node
        print('element has pushed.')

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty.')
        else:
            nodeValue=self.LinkedList.head.data
            self.LinkedList.head=self.LinkedList.head.next
            print('Displaying removed element.')
            print(nodeValue)
    
    def peek(self):
        if self.isEmpty():
            print('Stack is Empty.')
        else:
            print('Displaying Top element.')
            print(self.LinkedList.head.data)

    def delete(self):
        self.LinkedList.head=None
        print('Linked List has Deleted.')
    
    # def display(self):
    #     if self.isEmpty():
    #         print('Stack is Empty')
    #     else:
    #         print('Display stack again')
    #         temp=self.LinkedList.head
    #         while temp is not None:
    #             print(temp.data)
    #             temp=temp.next
    #         print()
    


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
# customStack.display()
customStack.pop()
# customStack.display()
customStack.peek()