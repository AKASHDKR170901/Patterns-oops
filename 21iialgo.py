def isPalindrome(string):
    reversedchar=[]
    for i in reversed (range(len(string))):
        reversedchar.append(string[i])
    return string==''.join(reversedchar)