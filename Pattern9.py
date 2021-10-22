col=1
n=1
x=int(input('Enter End Range:'))
for i in range(1,x):
    for j in range(1,col+1):
        print(n,end=' ')
        n+=1
    col+=2
    print()