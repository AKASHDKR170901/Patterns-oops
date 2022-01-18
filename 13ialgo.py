class LinkedList:
    def __init__(self,value):
        self.value=value
        self.next=None
def removeDuplicatesFromLinkedList(linkedlist):
    currentnode=linkedlist
    while currentnode is not None:
        nextdistinctnode=currentnode.next
        while nextdistinctnode is not None and nextdistinctnode.value==currentnode.value:
            nextdistinctnode=nextdistinctnode.next
        currentnode.next=nextdistinctnode
        currentnode=nextdistinctnode
    return linkedlist
