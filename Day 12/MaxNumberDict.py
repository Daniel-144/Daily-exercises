"""
Problem #2
Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
output can be in any order.
eg input = [1,1,1,2,2,3,5,5,5,5], k =2
output [1,5] (top 2 most frequently occuring numbers)
input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
output [4,5,3,1]
"""
# initializing a dictionary.
noOfFreq={}
# input the sequence of number with spaces.
list1=input("enter the sequence with spaces:")
# splitting and mapping them into integers.
list1=list(map(int,list1.split(" ")))
k=int(input("enter any number:"))
# storing the numbers and its frequency into list.
for number in list1:
    if number in noOfFreq:
        noOfFreq[number]+=1
    else:
        noOfFreq[number]=1
# sorting the dictionary in decending order based on the no of frequency in descending order
noOfFreq= sorted(noOfFreq.items(),key=lambda x:x[1],reverse=True)
# storing the number of top frequencies in list called as op.
op=[x[0] for x in noOfFreq[:k]]
print(f"the numbers with top {k} frequency are : {op}")

"""
OP:
enter the sequence with spaces:1 1 1 1 2 2 3 3 3 4 4 4 4 4
enter any number:2
[1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
the numbers with top 2 frequency are : [4,1]

enter the sequence with spaces:1 1 1 1 2 2 2 3 3 3 3 5 5 5 1
enter any number:2
the numbers with top 2 frequency are : [1,3]

enter the sequence with spaces:1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6
enter any number:4
the numbers with top 4 frequency are : [6, 5, 4, 3]
"""

