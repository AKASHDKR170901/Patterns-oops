class student:
    def __init__(self):
        self.name='Akash'
        self.roll=11
        self.marks=99
    def talk(self):
        print('My name is:',self.name)
        print('My rollno is:', self.roll)
        print('My marks are:', self.marks)
s=student()
print(s.name)
print(s.roll)
print(s.marks)
s.talk()