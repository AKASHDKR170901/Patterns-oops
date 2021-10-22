class Test:
    def __init__(self):
        self.x=10
t1=Test()
t2=Test()
print(t1.x,t2.x)
t1.x=888
print(t1.x,t2.x)

