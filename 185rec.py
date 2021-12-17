class Test:
    def __init__(self,name):
        self.name=name
t=Test('Durga')
print(t.name)
t.__init__('sunny')
print(t.name)