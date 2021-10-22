print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
print("Choose what is ur choice by typing nos from 1 to 4:\n")
c=eval(input("Enter choice:"))
a=eval(input("Enter 1st number:"))
b=eval(input("Enter 2nd number:"))
if c==1:
    print("Sum of the nos is:",a+b)
if c==2:
    if a>b:
        print("Difference of the nos is:",a-b)
    else:
        print("Difference of the nos is:",b-a)
if c==3:
    print("Product of the nos is:",a*b)
if c==4:
    if b==0:
        print("zero division error")
    else:
        print("Division of the nos is:",a/b)


