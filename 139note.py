class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self):
        self.d=40
        Test.e=50
    @classmethod
    def m2(cls):
        cls.f=60
        Test.g=70
    @staticmethod
    def m3():
        Test.h=80
t=Test()
t.m1()
Test.m2()
Test.m3()
Test.i=90
print(Test.__dict__)
print(t.a,t.c,t.e,t.f,t.g,t.h,t.i)
print(Test.a,Test.c,Test.e,Test.f,Test.g,Test.h,Test.i)
