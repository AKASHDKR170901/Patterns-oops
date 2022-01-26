def firstNonRepeatingCharacter(string):
    charactercount={}
    for character in string:
        charactercount[character]=charactercount.get(character,0)+1
    for i in range(len(string)):
        character=string[i]
        if charactercount[character]==1:
            return i
    return -1



