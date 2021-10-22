class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
        print('constructor executed')
    def display(self):
        print('Employee no:',self.eno)
        print('Employee name:', self.ename)
e1=Employee(100,'durga')
e2=Employee(200,'ak')
e1.display()
e2.display()