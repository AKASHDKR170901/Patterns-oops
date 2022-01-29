def smallestDifference (array1, array2):
    array1.sort()
    array2.sort()
    i = 0
    j = 0
    smallest = float('inf')
    current = float('inf')
    smallestpair = []
    while i < len(array1) and j < len(array2):
        firstno = array1[i]
        secondno = array2[j]
        if firstno < secondno:
            current = secondno-firstno
            i += 1
        elif secondno < firstno:
            current = firstno-secondno
            j += 1
        else:
            return [firstno, secondno]
        if smallest > current:
            smallest = current
            smallestpair = [firstno, secondno]
    return smallestpair
