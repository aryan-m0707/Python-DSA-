import sys

class Queue:

  def __init__(self, size):
    self.myQueue = []
    self.queueSize = size
    
  def isFull(self):
    if len(self.myQueue) == size:
      return True
    else:
      return False
      
  def enQueue(self, value):
    if self.isFull():
      print("Queue is already Full")
    else:
      self.myQueue.append(value)

  def display(self):
    print(self.myQueue)

  def isEmpty(self):
    if self.myQueue == []:
      return True
    else:
      return False

  def deQueue(self):
    if self.isEmpty():
      print("Given queue is Empty")
    else:
      self.myQueue.pop(0)

size = int(input("Please enter the size of the Queue:"))
obj = Queue(size)

print("Stack has been Created")

while True:
  print("Queue Operation:")
  
  print("1. Enqueue Operation")
  print("2. Display Queue:")
  print("3. Dequeue Operation:")
  print("4. Peek Operation:")
  print("5. Delete Queue:")
  print("6. Exit")
  
  choice = int(input("Enter your choice:"))

  if choice == 1:
    value = int(input("Enter an Element to add in the Queue:"))
    obj.enQueue(value)
  elif choice == 2:
    obj.display()
  elif choice == 3:
    obj.deQueue()