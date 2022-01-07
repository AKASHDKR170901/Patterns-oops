class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def branchSums(root):
    sums=[]
    calculatebranchsums(root,0,sums)
    return sums
def calculatebranchsums(node,runningsum,sums):
    if node is None:
        return
    newrunningsum=runningsum+node.value
    if node.left is None and node.right is None:
        sums.append(newrunningsum)
        return
    calculatebranchsums(node.left,newrunningsum,sums)
    calculatebranchsums(node.right,newrunningsum,sums)



