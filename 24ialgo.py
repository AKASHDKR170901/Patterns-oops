def generateDocument(characters,document):
    for character in document:
        documentfrequency=countcharacterfrequency(character,document)
        charactersfrequency=countcharacterfrequency(character,characters)
        if documentfrequency>charactersfrequency:
           return False
    return True
def countcharacterfrequency(character,target):
    frequency=0
    for char in target:
        if char==character:
            frequency+=1
    return frequency




