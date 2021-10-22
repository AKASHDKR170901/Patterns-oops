def sum(name,*n):
    result=0
    for x in n:
        result=result+x
    print("Sum of",name,"is",result)
sum("durga")
sum("akash",10)
sum("vino",10,20)
sum("siva",10,20,30)
sum("fg",10,20,30,40)