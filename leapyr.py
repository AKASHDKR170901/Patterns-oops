y=int(input("Enter year:"))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("{0} is a leap year".format(y))
        else:
            print("{0} is a non-leap year".format(y))
    else:
        print("{0} is a non-leap year".format(y))        
else:
    print("{0} is a non-leap year".format(y))        