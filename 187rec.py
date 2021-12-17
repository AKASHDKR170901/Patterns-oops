class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def get_bonus(self):
        bonus=self.salary*0.1
        return bonus
e=Employee('Durga',60,10000)
print(e.get_bonus())
