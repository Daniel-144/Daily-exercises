"""
Problem #1
Write a program to check if a given string of parentheses, Brackets, and braces is balenced.
For instance, "({[]}) is balanced, but "({[)})" is not balanced.
Input - (abc[i]) or (Abc[2])
Output true
Input - ((Abc[i]) or (Abc[2])))
Output False
"""

def CheckingTheBalanceOfTheString(string,opening,closing):
    checkingList=[]
    for char in string:
        if char in opening:
            checkingList.append(char)
        elif char in closing:
            if checkingList and checkingList[-1] == opening[closing.index(char)]:
                checkingList.pop()
    if not checkingList:
        return(True)
    else:
        return(False)


string=input("enter a string with a sequence of parantheses, brackets, braces (example:(a[i])):")
# initializing a list of open characters.
opening=["{","(","["]
# initializing a list of close characters.
closing=["}",")","]"]
output=CheckingTheBalanceOfTheString(string,opening,closing)
if output == True:
    print("the parantheses and brackets are balanced!!")
else:
    print("the parantheses and brackets are not balanced!!")