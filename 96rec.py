n=int(input("Enter no.of students:"))
d={}
for i in range(n):
    name=input("Enter name:")
    marks=eval(input("Enter marks:"))
    d[name]=marks
print(d)
while True:
    name=input("Enter students name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student name is unavailable")
    else:
        print("Marks of {} is {}".format(name,marks))
        option=input("Do you want to find another student mark[yes/No]")
        if option=='no':
            break
print("Thanks for using our application")