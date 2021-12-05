class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print('Hello I am:',self.name)
        print('My rollno is:', self.rollno)
        print('My marks is:', self.marks)
s1=student('sunny',101,90)
print('student1:',s1.name,s1.rollno,s1.marks)
s2=student('Bunny',102,91)
print('student2:',s2.name,s2.rollno,s2.marks)
