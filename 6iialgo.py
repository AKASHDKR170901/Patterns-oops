def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,tree.value)
def findClosestValueInBstHelper(tree,target,closest):
    currentnode=tree
    while currentnode is not None:
        if abs(target-closest)>abs(target-currentnode.value):
            closest=currentnode.value
        if target<currentnode.value:
            currentnode=currentnode.left
        elif target>currentnode.value:
            currentnode=currentnode.right
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
