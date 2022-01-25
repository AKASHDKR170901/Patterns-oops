def generateDocument(characters,document):
    alreadycounted=set()
    for character in document:
        if character in alreadycounted:
            continue
        documentfrequency=countcharacterfrequency(character,document)
        charactersfrequency=countcharacterfrequency(character,characters)
        if documentfrequency>charactersfrequency:
            return False
        alreadycounted.add(character)
    return True
def countcharacterfrequency(character,target):
    frequency=0
    for char in target:
        if char==character:
            frequency+=1
    return frequency
