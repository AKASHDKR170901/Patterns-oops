from sys import argv
args=argv[1:]
sum=0
for x in args:
    n=int(x)
    sum+=n
    print("The sum is:",sum)
