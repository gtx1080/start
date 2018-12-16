class tree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.cargo)
    '''
    def printtree(self):
        self.printout(self.cargo)
    def printout(self,comin):
        if comin is None:
            return 0
        return printout(self.left), printout(self.right), comin
        '''
def printtreein(tree1):
    if tree1 is None:
        return
    printtreein(tree1.left())
    print(tree1.cargo,end='')
    printtreein(tree1.right())
t1=tree("a",tree('b',tree('d'),'c'))
printtreein(t1)