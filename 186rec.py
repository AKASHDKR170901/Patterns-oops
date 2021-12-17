class Test:
    def __init__(self,name):
        self.name=name
class Demo:
    def __init__(self,name):
        self.name=name
t=Test('Sunny')
d=Demo('Bunny')
t.__init__('Lunny')
d.__init__('Munny')