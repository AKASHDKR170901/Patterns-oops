import emp,pickle
f=open("emp.dat","wb")
n=int(input('Enter no of employees:'))
for i in range(n):
    eno=int(input("Enter employee number:"))
    ename=input("Enter employee name:")
    esal=float(input("Enter employee salary "))
    eaddr=input("Enter employee address:")
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
