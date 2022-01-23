class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print('*'*30)
        print('Employee no:',self.eno)
        print('Employee name:',self.ename)
        print('Employee salary:',self.esal)
        print('Employee address:',self.eaddr)
        print('*'*30)
e1=Employee(100,'DURGA',2000,'Hyd')
e2=Employee(101,'AKASH',3000,'Tn')
e1.info()
e2.info()
