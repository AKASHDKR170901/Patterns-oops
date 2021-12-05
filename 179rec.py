class student:
    def __init__(delf,name,rollno,marks):
        delf.name=name
        delf.rollno=rollno
        delf.marks=marks
    def talk(kelf):
        print('Hello I am:',kelf.name)
        print('My rollno is:',kelf.rollno)
        print('My marks is:',kelf.marks)
s1=student('sunny',101,90)
print('student1:',s1.name,s1.rollno,s1.marks)
s2=student('Bunny',102,91)
print('student2:',s2.name,s2.rollno,s2.marks)
s1.talk()
s2.talk()
