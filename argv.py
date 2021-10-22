from sys import argv
print("The no of command line arguements:",len(argv))
print("The list of command line arguements:",argv)
print("Command line arguements one by one:")
for x in argv:
    print(x)
print("slice operator result:",argv[1:3])
