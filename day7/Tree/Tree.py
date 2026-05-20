# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]

#     def addChild(self, object):
#         self.child.append(object)
#         print('Tree node Added')

#     def __str__(self, level = 0):
#         ret=' ' * level+str(self.data)+'\n'
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret

# rootnode=Tree('Drinks')
# hot=Tree('Hot')
# cold=Tree('Cold')
# tea=Tree('Tea')
# coffee=Tree('Coffee')
# nonAlcholic=Tree('non Alcholic')
# alcholic=Tree('Alcholic')

# rootnode.addChild(hot)
# rootnode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(nonAlcholic)
# cold.addChild(alcholic)

# print(rootnode)
# # when we print any object , then the string fuction call automaticaly
 


class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def addChild(self, object):
        self.child.append(object)
        print('Tree node Added')

    def __str__(self, level = 0):
        ret=' ' * level+str(self.data)+'\n'
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret

rootnode=Tree('Drinks')
hot=Tree('Hot')
cold=Tree('Cold')
tea=Tree('Tea')
coffee=Tree('Coffee')
nonAlcholic=Tree('non Alcholic')
alcholic=Tree('Alcholic')

rootnode.addChild(hot)
rootnode.addChild(cold)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(nonAlcholic)
cold.addChild(alcholic)

print(rootnode)
# when we print any object , then the string fuction call automaticaly
 