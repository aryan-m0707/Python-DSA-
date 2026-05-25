class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.matrix=[[0 for _ in range(vertices)]
                     for _ in range(vertices)]
    
    def printMatrix(self):
        print('Adjacency Matrix.')
        for i in self.matrix:
            print(i)

    def add_edges(self,vertex1,vertex2):
       self.matrix[vertex1][vertex2]=1 
       self.matrix[vertex2][vertex1]=1 

    def remove_edges(self,vertex1,vertex2):
       self.matrix[vertex1][vertex2]=0
       self.matrix[vertex2][vertex1]=0 

obj=Graph(4)
# obj.printMatrix()
obj.add_edges(0,1)
obj.add_edges(0,2)
obj.add_edges(1,3)
obj.add_edges(2,3)
obj.printMatrix()
# obj.remove_edges(3,1)
# obj.printMatrix()