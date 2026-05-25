class HashTable:
    def __int__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hash_function(self,key):
        return key % self.size

    def insert(self,key):
        index=self.hash_function(key)
        self.table[index].append(key)
    
    def display(self):
        print(self.table)

obj=HashTable(4)
obj.insert(10)
obj.display()
