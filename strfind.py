s=input("Enter a main string:")
sub=input("Enter a sub string:")
l=len(s)
i=s.find(sub)
if i==-1:
    print(sub,"is not present in",s)
while i!=-1:
    print(sub,'present at index:',i)
    i=s.find(sub,i+len(sub),l)
print("No of occurences:",s.count(sub))
