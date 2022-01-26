def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        foundduplicate=False
        for j in range(len(string)):
            if string[i]==string[j] and i!=j:
                foundduplicate=True
        if not foundduplicate:
            return i
    return -1