class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def addNode(self, val):
    self.node = Node(val)
    if self.head is None:
      self.head = self.node
      self.head = self.node
    else:
      self.tail.next = self.node
      self.tail      = self.node
  
  def displayNode(self):
    while self.head is not None:
      print(self.head.data, '|', '->', end=' ')
      self.head = self.head.next
  
  def addNodeBeginning(self, val):
    print("Add a Node at the Beginning")
    self.node = Node(val)
    if self.head is None:
      self.head = self.node
      self.tail = self.node
    else:
      self.node.next = self.head
      self.head = self.node
  
if __name__ == '__main__':
  obj = LinkedList()
  
  while True:
    print("1. Add a Node in the Linked List:")
    print("2. Add a Node in the Beginning of the Linked List:")
    print("3. Add a Node in Between of the Linked List:")
    print("4. Add a Node in the End of the Linked List:")
    print("5. Display the Linked List")
    print("6. Exit")
    
    ch = int(input("Enter an Option: "))
    
    if ch == 1:
      val = int(input("Enter a Value for the Node: "))
      obj.addNode(val)
      print("Node Added Successfully in a Single Linked List")
    elif index = 0:
        node.next = self.head
        self.head = node

    else self.head
      for_ in range(index-1)
      displayNode(obj)