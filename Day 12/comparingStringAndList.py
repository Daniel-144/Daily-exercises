"""
you have a list of unique words. you input is a string with no spaces. Return true if the letters in the
inpot string can be separated into words that are into words that are in list.
eg list=["we","students","are"]
input="we are students"
output=True

eg 2 list =["we","doctor","and","nurse","are"]
input = "wearenurseandoctor"
output = False.
input = "wearenurseanddoctor"
output = True
"""
# to compare the length of the string and the contents of the list.
def CompareOfLength(listOfWords,inpStr):
    length=0
    for i in listOfWords:
        length+=len(i)
    if (length == len(inpStr)):
        return True
    return False
    
# checking if the both words are same.
def ContentsOfTheListAreInStringOrNot(string,i):
    if(string == i):
        return True
    return False

# geting the list from the user.
listOfWords=input("enter the words which will be in the upcoming string(please enter with spaces):").lower()
listOfWords=listOfWords.split(" ")
# geting the input string.
inpStr=input("enter the string:")
inpStr=inpStr.lower()

#printing the input list and string
print("input:",listOfWords)
print("InputString:",inpStr)

# checking if the length of the words inside the List.
if (CompareOfLength(listOfWords,inpStr)==True):
    for i in range(len(listOfWords)):
        for words in listOfWords:
            # checking if the both strings are same.
            if (ContentsOfTheListAreInStringOrNot(inpStr[0:len(words)],words)==True):
                inpStr=inpStr[len(words):]
        # if the string becomes an empty string
        if not inpStr:
            break

# predicting the output.
if not inpStr:
    print("True")
else:
    print("False")

"""
Op
1)enter the words which will be in the upcoming string(please enter with spaces):we doctor and nurse are
enter the string:wearenurseandoctor 
input: ['we', 'doctor', 'and', 'nurse', 'are']
InputString: wearenurseandoctor
False

2)enter the words which will be in the upcoming string(please enter with spaces):we doctor and nurse are
enter the string:wearedoctorandnurse
input: ['we', 'doctor', 'and', 'nurse', 'are']
InputString: wearedoctorandnurse
True

3)enter the words which will be in the upcoming string(please enter with spaces):we students are
enter the string:wearestudents
input: ['we', 'students', 'are']
InputString: wearestudents
True
"""




