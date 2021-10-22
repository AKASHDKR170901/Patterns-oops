s=input("Enter some string:")
n=len(s)
i=0
print()
print("Data in frwd direction:")
while i<n:
    print(s[i],end='')
    i+=1
print()
print("Data in bkwd direction:")
while i>n:
    print(s[i],end='')
    i-=1
