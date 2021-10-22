class se:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech
s1=se('durga',48,'python')
s2=se('ak',30,'c')
s1.gf='sunny'
s2.gf='mallika'
s1.brand='rc'
s2.brand='re'
print(s1.__dict__)
print(s2.__dict__)

