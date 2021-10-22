l=[1,2,3,4,5,6,]
target=int(input("Enter the value to search:"))
try:
    print(target,"available and its first occurence is at:",l.index(target))
except ValueError:
    print(target,"not available")
