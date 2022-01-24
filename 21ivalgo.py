def isPalindrome(string,i=0):
    leftidx=0
    rightidx=len(string)-1
    while leftidx<rightidx:
        if string[leftidx]!=string[rightidx]:
            return False
        leftidx+=1
        rightidx-=1
    return True
