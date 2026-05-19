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

  

size = int(input("Please enter the size of the Queue:"))
obj = Queue(size)

print("Stack has been Created")

while True:
  print("1. Operation:")
  print("2. Display Queue:")
  print("3. Pop Operation:")
  print("4. Peek Operation:")
  print("5. Delete Queue:")
  print("6. Exit")
  
  choice = int(input("Enter your choice:"))

  if choice == 1:
    value = int(input("Enter the value to be inserted:"))
    obj.enQueue(value)