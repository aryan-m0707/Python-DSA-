class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif rootNode.data >= nodeValue:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue) 
        else:
            insertNode(rootNode.rightChild,nodeValue)

def PreOrderTraversal(rootNode):
    if rootNode is None: # if not rootNode
        return 
    print(rootNode.data,end=' ')
    PreOrderTraversal(rootNode.leftChild)
    PreOrderTraversal(rootNode.rightChild)        

def PostOrderTraversal(rootNode):
    if rootNode is None:
        return 
    PreOrderTraversal(rootNode.leftChild)
    PreOrderTraversal(rootNode.rightChild) 
    print(rootNode.data,end=' ')

def InOrderTraversal(rootNode):
    if rootNode is None:
        return 
    PreOrderTraversal(rootNode.leftChild)
    print(rootNode.data,end=' ')
    PreOrderTraversal(rootNode.rightChild) 

def SearchNode(rootNode,value):
    if rootNode.data == value:
        print('Node found')
    elif rootNode.data > value:
        if rootNode.data == value:
            print('node Found')
        else:
            if rootNode.leftChild is None:
                print('not found')
            else:
                SearchNode(rootNode.leftChild,value)
    elif rootNode.data < value:
        if rootNode.data == value:
            print('node Found')
        else:
            if rootNode.rightChild is None:
                print('not found')
            else:
                SearchNode(rootNode.rightChild,value)
    else:
        print('node not found')

newBST=BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
insertNode(newBST,10)

# print('Pre-Order Traversal :')
# PreOrderTraversal(newBST)
# print()
# print('Post-Order Traversal :')
# PostOrderTraversal(newBST)
# print()
# print('In-Order Traversal :')
# InOrderTraversal(newBST)
# print()

SearchNode(newBST,210)
