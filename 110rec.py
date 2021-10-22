def outer():
    print("Outer function started")
    def inner():
        print("Inner function execution")
    print("Outer function returning")
    return inner
f1=outer()
f1()