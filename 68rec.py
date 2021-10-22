s=input("Enter some string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        newch=chr(ord(previous)+int(x))
        output=output+newch
print(output)