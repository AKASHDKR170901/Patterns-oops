def decor(func):
    def inner(name):
        if name=='sunny':
            print("Hello sunny bad morning....")
        else:
            func(name)
        return inner
@decor
def wish(name):
    print("Hello","name","Good morning")
wish("Durga")
wish("Ravi")
wish("sunny")
wish("Mallika")
wish("Akash")
wish("Divyakumar")
wish()



def decor(func):
    def inner(name):
        if name=='sunny':
            print("Hello sunny bad morning....")
        else:
            func(name)
        return inner
@decor
def wish(name):
    print("Hello","name","Good morning")
wish("piyush")
wish("lisa")
wish("ponu")
wish("Mint")
wish("Rin")
wish("Bind")
wish("Erita")