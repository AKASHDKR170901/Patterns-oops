def generateDocument(characters,documents):
    charactercount={}
    for character in characters:
        if character not in charactercount:
            charactercount[character]=0
        charactercount[character]+=1
    for character in documents:
        if character not in charactercount or charactercount[character]==0:
            return False
        charactercount[character]-=1
    return True


