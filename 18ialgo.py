def bubbleSort(array):
    issorted=False
    counter=0
    while not issorted:
        issorted=True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                issorted=False
        counter+=1
    return array
