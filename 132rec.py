class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def m1(self):
        self.c=3000
        self.d=4000
t1=Test()
t1.m1()
t1.a=77
t1.e=88
t1.f=99
print(t1.__dict__)
t2=Test()
print(t2.__dict__)
