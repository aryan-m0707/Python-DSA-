import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addNode(self,value):
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail=self.node
    
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end=' ')
            temp=temp.next
        print()

    def addBeg(self,val):
        self.node=Node(val)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node
            print('added')
    

        

if __name__=='__main__':
    object=LinkedList()

    while True:
        print('1. Add Node LinkedList :')
        print('2. Add Node in Begining :')
        print('3. Add Node in Between :')
        print('4. Add Node in end :')
        print('5. Display LinkedList :')
        print('6. Exit :')
        ch=int(input('Enter your choice :'))
        if ch == 1:
            value=int(input('Enter value for node :'))
            object.addNode(value)
            print('Node added successfully')
        elif ch == 2:
            value=int(input('Enter value for node :'))
            object.addBeg(value)
            print('Node added successfully')
        elif ch == 3:
            value=int(input('Enter value for node :'))
            object.addNode(value)
            print('Node added successfully')
        elif ch == 4:
            value=int(input('Enter value for node :'))
            object.addNode(value)
            print('Node added successfully')
        elif ch == 5:
            object.display()
        elif ch == 6:
            sys.exit()
        