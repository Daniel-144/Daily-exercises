"""
Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]
"""
# enter values with duplicates.
LengthOfList=int(input("Enter the no of elements you want to enter in the list:"))
ListOfNumbers=[]
for i in range(LengthOfList):
    elements=int(input("Enter the Value to append in the list:"))
    ListOfNumbers.append(elements)
print(f"Input List:{ListOfNumbers}")
ListOfNumbers.sort(reverse=True)
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
OP:
Enter the no of elements you want to enter in the list:10
Enter the Value to append in the list:1
Enter the Value to append in the list:2
Enter the Value to append in the list:3
Enter the Value to append in the list:3
Enter the Value to append in the list:3
Enter the Value to append in the list:4
Enter the Value to append in the list:4
Enter the Value to append in the list:7
Enter the Value to append in the list:7
Enter the Value to append in the list:9
Input List:[1, 2, 3, 3, 3, 4, 4, 7, 7, 9]
Output LIst:[9, 7, 4, 3, 2, 1, '_', '_', '_', '_']
"""