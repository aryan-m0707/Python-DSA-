import sys
class Queue:
    def __init__(self, size):
        self.myQueue=[]
        self.queueSize=size

    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def enqueue(self, val):
        if self.isFull():
            print('Queue is Full.')
        else:
            self.myQueue.append(val)
            print('Element has inserted.')

    def displayQueue(self):
        print(self.myQueue)

    def dequeue(self):
        if self.isEmpty():
            print('Queue is Empty.')
        else:
            # self.myQueue.remove(self.myQueue[0])
            self.myQueue.pop(0)
            print('Element has deleted.')

    def peek(self):
        if self.isEmpty():
            print('Queue is Empty.')
        else:
            print(self.myQueue[0])

    def deleteQueue(self):
        # self.myQueue=[]
        del self.myQueue
        print('Queue has deleted.')
    

size=int(input('Enter the size of queue: '))
objQueue = Queue(size)
print('Queue has created.')

while True:
    print('Queue operations.')
    print('1. Enqueue Operation')
    print('2. Display Queue')
    print('3. Dequeue Operation')
    print('4. Peek Operation')
    print('5. Delete Queue')
    print('6. Exit')
    choice=int(input('Enter your choice: '))
    if choice == 1:
        value=int(input('Enter the element for insertion: '))
        objQueue.enqueue(value)
    elif choice == 2:
        objQueue.displayQueue()
    elif choice == 3:
        objQueue.dequeue()
    elif choice == 4:
        objQueue.peek()
    elif choice == 5:
        objQueue.deleteQueue()
    elif choice == 6:
        sys.exit()