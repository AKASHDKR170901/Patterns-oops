s=input("Enter some string:")
i=0
print("Characters at even position:")
while i<len(s):
    print(s[i],end='')
    i=i+2
print()
print("Characters at odd position:")
i=1
while i<len(s):
    print(s[i],end='')
    i=i+2
