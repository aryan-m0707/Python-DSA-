class Grap:
    def __init__(self):
        self.adjacency_list={}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    
    def print_graph(self):
        # print(self.adjacency_list)
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for key in self.adjacency_list:
                if vertex in self.adjacency_list[key]:
                    self.adjacency_list[key].remove(vertex)
            
            self.adjacency_list.pop(vertex)
        else:
            print('Vertex not found.')

    
    # def add_connections(self):
    #     print('Enter 1 for exit.')
    #     while True:
    #         vertex=input('Enter vertex: ')
    #         if vertex not in self.adjacency_list.keys():
    #             self.adjacency_list[vertex]=[]
    #             print('vertex added')
    #         else:
    #             print('Vertex found.')
    #         val=input('Enter connected vertex: ')
    #         self.adjacency_list[vertex].append(val)
            

objGraph=Grap()
objGraph.add_vertex('A')
objGraph.add_vertex('B')
objGraph.add_vertex('C')
objGraph.add_vertex('D')
objGraph.add_vertex('E')
# objGraph.print_graph()
objGraph.add_edge('A','B')
objGraph.add_edge('A','C')
objGraph.add_edge('A','D')
objGraph.add_edge('B','A')
objGraph.add_edge('B','E')
objGraph.add_edge('C','A')
objGraph.add_edge('C','D')
objGraph.add_edge('D','A')
objGraph.add_edge('D','C')
objGraph.add_edge('D','E')
objGraph.add_edge('E','B')
objGraph.add_edge('E','D')
objGraph.print_graph()
print()
objGraph.remove_vertex('E')
objGraph.print_graph()
