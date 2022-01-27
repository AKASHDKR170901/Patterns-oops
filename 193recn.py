class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print('Hello my name is:',self.name)
        print('My age is:',self.age)
        print('My marks are:',self.marks)
s1=student('sunny',36,89)
s1.talk()
print()
s2=student('akash',21,199)
s2.talk()
