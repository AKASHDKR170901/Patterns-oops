class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("Enter age:"))
if age>60:
    raise TooYoungException("Plz wait for some more time definitely will get best pair in heaven")
elif age<18:
    raise TooOldException("Your age has already crossed the marriage ae no chance of getting marriage")
else:
    print("Thanks for registration...You will get match details by mail")
    
