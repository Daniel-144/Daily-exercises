"""
Problem #1
Write a program to check if a given string of parentheses, Brackets, and braces is balenced.
For instance, "({[]}) is balanced, but "({[)})" is not balanced.
Input - (abc[i]) or (Abc[2])
Output true
Input - ((Abc[i]) or (Abc[2])))
Output False
"""
# imported re
import re

# function to check if the given string is balanced.
def CheckingTheBalance1(string,opening,closing):
    # using regex sub function to substitute the characters other then the given charcter as ""
    tempString=re.sub(r'[^[\]{}()]','',string)
    # converting the string to list using th3e list function.
    tempString=list(tempString)
    # initializing a string to check if the string is balanced.
    checkList=[]

    # loop to check if the string is balanced.
    for i in tempString:
        if i in opening:
            # storing the index of the given character(opening list) in a variable called index.
            index=opening.index(i)
            # check if the closing of the parantheses or bracket is present in the list.
            if closing[index] in checkList:
                # pop the character from the list.
                checkList.pop()
            # if it is not present append the character in the list.
            else:
                checkList.append(i)
        elif i in closing:
            # storing the index of the given character(closing list) in a variable called index.
            index=closing.index(i)
            # check if the opening of the parantheses in the list.
            if opening[index] in checkList:
                # pop the character from the list.
                checkList.pop()
            # if it is not present append the character in the list.
            else:
                checkList.append(i) 
    # if the list is empty.
    if not checkList:
        # return True to the main function.
        return (True)
    # if the list is not empty
    else:
        # return False to the main function.
        return (False)




# getting a string with a combination of letter, numbers, brackets, paranthesis, braces from the user. 
string=input("enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):")
# initializing a list of open characters.
opening=["{","(","["]
# initializing a list of close characters.
closing=["}",")","]"]
# calling a function to check if the string is balanced.
output=CheckingTheBalance1(string,opening,closing)


# if the returned value is True then the string is balanced.
if output == True:
    print(f"the given string: {string} is a balanced string!!")
# if the returned value is False then the string is not balanced.
else:
    print(f"The given string: {string} is not a balance string!!")

"""
OP:
1)enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):(abc[i])
the given string: (abc[i]) is a balanced string!!

2)enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):(abc[i))
The given string: (abc[i)) is no a balance string!!

3)enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):))a]i[((
the given string: ))a]i[(( is a balanced string!!

4)enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):(a[i]])
The given string: (a[i]]) is not a balance string!!

"""