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
doubles(numbers)
squares(numbers)
endtime=time.time()
print('Time taken:',endtime-begintime)

