def isPalindrome(string):
    reversedstring=''
    for i in reversed (range(len(string))):
        reversedstring+=string[i]
    return string==reversedstring