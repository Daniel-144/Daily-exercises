"""
Problem #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed 
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]
"""
# enter values with duplicates.
LengthOfList=int(input("Enter the no of elements you want to enter in the list:"))
ListOfNumbers=[]
for i in range(LengthOfList):
    elements=int(input("Enter the Value to append in the list:"))
    ListOfNumbers.append(elements)
print(f"Input List:{ListOfNumbers}")
ListOfNumbers.sort()
prev=None
opList=[]
count=0
for num in ListOfNumbers:
    if num != prev:
        prev=num
        opList.append(num)
    else:
        count+=1
for j in range(count):
    opList.append('_')
print(f"Output LIst:{opList}")

"""
Op:
Enter the no of elements you want to enter in the list:8
Enter the Value to append in the list:3
Enter the Value to append in the list:4
Enter the Value to append in the list:9
Enter the Value to append in the list:0
Enter the Value to append in the list:8
Enter the Value to append in the list:9
Enter the Value to append in the list:0
Enter the Value to append in the list:1
Input List:[3, 4, 9, 0, 8, 9, 0, 1]
Output LIst:[0, 1, 3, 4, 8, 9, '_', '_']
"""