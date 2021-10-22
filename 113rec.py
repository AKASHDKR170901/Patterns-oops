import time
from imp import reload
import module1
print("Program entering into sleeping state")
time.sleep(30)
reload(module1)
print("Program entering sleep state again")
time.sleep(30)
reload(module1)
print("This is the last line of the program")
