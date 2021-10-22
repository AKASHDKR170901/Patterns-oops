from threading import*
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Doubles:',2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Squares:',n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('Time taken:',endtime-begintime)
