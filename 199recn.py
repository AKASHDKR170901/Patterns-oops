class A:
    def feature1(self):
        print('F1 working')
    def feature2(self):
        print('F2 working')
class B(A):
    def feature3(self):
        print('F3 working')
    def feature4(self):
        print('F5 working')
a1=A()
a1.feature1()
a2=A()
a2.feature2()
class C(A,B):
    def __init__(self):
        super().__init__()
        print('in C init')
    def feat(self):
        super().feature2()
a1=C()
a1.feat()
