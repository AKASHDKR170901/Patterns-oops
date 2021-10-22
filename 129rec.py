class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print('student name:',self.name)
        print('student rollno:',self.rollno)
        print('student marks:',self.marks)
        print()
s1=student('durga',101,90)
s2=student('Ak',102,93)
s3=student('kp',103,92)
s1.display()
s2.display()
s3.display()
print(s1.name,s1.rollno,s1.marks)
print(s1.__dict__)
