t=eval(input("Enter some of the tuple of numbers:"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
print("Sum=",sum)
print("Average:",sum/l)