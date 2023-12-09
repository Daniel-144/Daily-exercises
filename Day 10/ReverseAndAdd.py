"""
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
"""

# function to add the characters of list 1 and 2.
def addContents(list1,list2):
    # initializing the empty list to store the result.
    result=[]
    # initializing sum
    sum=0
    for i in range(max(len(list1),len(list2))):
        if i < len(list1):
            num1=list1[i]
        else:
            num1=0
        if i < len(list2):
            num2=list2[i]
        else:
            num2=0
        total=num1+num2+sum
        result.append(total%10)
        sum=total//10
    if sum > 0:
        result.append(sum)
    return(result[::-1])

# sample inputs
list1=[1,2,3]
list2=[5,6,7]
# call the function called add contents
result=addContents(list1,list2)
print(result)