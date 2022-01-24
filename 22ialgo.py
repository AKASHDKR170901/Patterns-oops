def caesarCipherEncryptor(string,key):
    newletter=[]
    newkey=key%26
    for letter in string:
        newletter.append(getnewletter(letter,newkey))
    return ''.join(newletter)
def getnewletter(letter,key):
    newlettercode=ord(letter)+key
    return chr(newlettercode) if newlettercode<=122 else chr(96+ newlettercode%122)
