def getNthFib(n):
    lasttwo=[0,1]
    counter=3
    while counter<=n:
        nextfib=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=nextfib
        counter+=1
    return lasttwo[1] if n>1 else lasttwo[0]

