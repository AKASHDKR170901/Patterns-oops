s=input("Enter some string:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    if x.isdigit():
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

