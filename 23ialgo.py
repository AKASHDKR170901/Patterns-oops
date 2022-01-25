def runLineEncoding(string):
    encodedstringcharacters=[]
    currentrunlength=1
    for i in range(1,len(string)):
        currentcharacter=string[i]
        previouscharacter=string[i-1]
        if currentcharacter != previouscharacter or currentrunlength==9:
            encodedstringcharacters.append(str(currentrunlength))
            encodedstringcharacters.append(previouscharacter)
            currentrunlength=0
        currentrunlength+=1
    encodedstringcharacters.append(str(currentrunlength))
    encodedstringcharacters.append(string[len(string)-1])
    return ''.join(encodedstringcharacters)
