class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def m1(self):
        self.c=3000
        self.d=4000
t1=Test()
t1.m1()
print(t1.a,t1.b,t1.c,t1.d)
t2=Test()
t2.a=888
t2.b=999
t2.c=777
print(t2.__dict__)
