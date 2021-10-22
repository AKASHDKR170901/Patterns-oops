class Test:
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
        self.d=4
t1=Test()
t2=Test()
del t1.c
del t2.d
print('t1:',t1.__dict__)
print('t2:',t2.__dict__)
