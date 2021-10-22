import logging
logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info('Anew request came')
try:
    x=int(input('Enter 1st no:'))
    y=int(input('Enter 2nd no:'))
    print(x/y)
except ZeroDivisionError as msg:
    print('cannot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('Enter only int values')
    logging.exception(msg)
logging.info('Request Processing completed')
