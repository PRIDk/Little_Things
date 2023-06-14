def caseSensitive(firstStr, secondStr):
    if firstStr == secondStr:
        return("Same strings!")
    else: 
        return("Different strings!")

def notCaseSensitive(firstStr, secondStr): # good for SHA256 etc.
    firstStr = allUpper(firstStr)
    secondStr = allUpper(secondStr)
    if firstStr == secondStr:
        return("Same strings!")
    else: 
        return("Different strings!")

def allUpper(string):
    return [x.upper() for x in string]
        
def whichMethod(which, firstStr, secondStr):
    if which == "y":
        print(caseSensitive(firstStr, secondStr))
    else: print(notCaseSensitive(firstStr, secondStr))

first = input("Input 1st string: ")
second = input("Input 2nd string: ")
whichOne = input("Do you want them to be check with case sensitivity or not? (y/n): ")

print(whichMethod(whichOne, first, second))