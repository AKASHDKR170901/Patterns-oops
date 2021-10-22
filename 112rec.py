def division(a,b):
    return a/b
print(division(10,2))
print(division(10,5))
print(division(10,0))
def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("Hey idiot")
            return
        else:
            return func(a,b)
    return inner
@smartdivision