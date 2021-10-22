import emp,pickle
f=open("emp.dat","rb")
print("Employee details......")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFERROR:
        print("All details are recorded.....")
        break
f.close()
