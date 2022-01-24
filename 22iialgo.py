def caesarCipherEncryptor(string,key):
    newletter=[]
    newkey=key%26
    alphabets=list('abcdefghijklmnopqrstuvwxyz')
    for letter in string:
        newletter.append(getnewletter(letter,newkey,alphabets))
    return ''.join(newletter)
def getnewletter(letter,key,alphabets):
    newlettercode=alphabets.index(letter)+key
    return alphabets[newlettercode%26]