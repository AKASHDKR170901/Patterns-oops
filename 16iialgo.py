def binarySearch(array,target):
    return binarySearchHelper(array,target,0,len(array)-1)
def binarySearchHelper(array,target,left,right):
    while left<=right:
        middle=(left+right)//2
        potentialmatch=array[middle]
        if target==potentialmatch:
            return middle
        elif target<potentialmatch:
            right=middle-1
        else:
            left=middle+1
    return -1
