class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def __str__(self,level=0):
        ret="   "*level+str(self.data)+"\n"
        for child in self.child:
            ret+=child.__str__(level+1)
        return ret

    def addChild(self,object):
        self.child.append(object)
    print("Tree Node Added")


rootNode=Tree("Drinks")
Hot=Tree("Hot")
Cold=Tree("Cold")
Tea=Tree("Tea")
Coffee=Tree("Coffee")
NonAlcoholic=Tree("Non-Alcoholic")
Alcoholic=Tree("Alcoholic")
GreenTea=Tree("Green Tea")
BlackTea=Tree("Black Tea")

rootNode.addChild(Hot)
rootNode.addChild(Cold)
Hot.addChild(Tea)
Hot.addChild(Coffee)
Cold.addChild(NonAlcoholic)
Cold.addChild(Alcoholic)
Tea.addChild(GreenTea)
Tea.addChild(BlackTea)

print(rootNode)