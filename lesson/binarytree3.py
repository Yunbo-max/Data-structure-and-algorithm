from pythonds.basic.stack import Stack
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def  insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key



import operator
def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRghtChild()

    if leftC and rightC:
        fn=opers[parseTree.getRootval()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def postordereval(tree):
    opers ={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1=None
    res2=None
    if tree:
        res1=postordereval(tree.getLeftChild())
        res2=postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
a=BinaryTree((3+4*5))
print(postordereval(a))




