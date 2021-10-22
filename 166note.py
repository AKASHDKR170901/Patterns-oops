from threading import*
class Mythread(Thread):
    def run(self):
        for i in range(10):
            print('Child thread')
t=Mythread()
t.start()
for i in range(10):
    print('Main thread')
