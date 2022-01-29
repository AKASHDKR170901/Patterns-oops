def moveElementToEnd(array,tomove):
    i=0
    j=len(array)-1
    while i<j:
        while i<j and array[j]==tomove:
            j-=1
        if array[i]==tomove:
            array[i],array[j]=array[j],array[i]
        i+=1
    return array