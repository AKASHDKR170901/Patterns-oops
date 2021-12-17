class Test:
    def __init__(self):
        print('Constructor execution...',id(self))
t=Test()
t.__init__()
t.__init__()
t.__init__()
