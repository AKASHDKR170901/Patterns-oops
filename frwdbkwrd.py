s=input("Enter some string:")
n=len(s)
i=0
print()
print("Data in forward direction:")
while i<n:
    print(s[i],end='')
    i+=1
print()
i=-1
print("Data in backward direction:")
while i>=-n:
    print(s[i],end='')
    i=i-1