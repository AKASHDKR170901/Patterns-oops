class student:
    school='Telusko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print('This is the student class in abc method')
s1=student(1,2,3)
s2=student(4,5,6)
print(s1.avg)
print(student.getschool())
student.info()


