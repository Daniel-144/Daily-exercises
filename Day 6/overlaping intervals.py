"""
Program 2
Given a collection of two numbers that specify an interval, merge all overlapping intervals. 
For example, 
Input [[1,3],[2,6],[8,10],[15,20],[16,25] ]
Output [[1,6],[8,10],[15,25]].
"""

# function to count the number of overlapping terms.
def NoOfOverlapping(interval):
    count=0
    # sorting the input based on the 1st digit of the sub-list using lambda function
    interval.sort(key= lambda x: x[0])
    # loop to count the number of overlapping terms. 
    for i in range(len(interval)-1):
        if interval[i][1] >= interval[i+1][0]:
            count+=1
    # returning the number of overlapping terms to the mainn function.
    return(count)

# function to pop the overlapping intervals
def PopIntervals(intervals):
    tempInterval=intervals
    # loop to traverse trhrough the list
    for j in range(len(tempInterval)-1):
        if j < len(tempInterval)-1:
            # to check if the sublist is within a domain of another sublist.
            if tempInterval[j][1] >= tempInterval[j+1][0] :
                # if the sublist is within the range of another sublist merge these two sublist.
                tempInterval[j][1] = tempInterval[j+1][1]
                # pop the 2nd sublist because we have the merged sublist.
                tempInterval.pop(j+1)
        else:
            # break if the value of j is greater than the length of the list.
            break
    # return the resultant list to the main  function.
    return(tempInterval)


# input sequence.
input_intervals = [[1,3],[2,6],[8,10],[15,20],[16,25] ]
print("Input:", input_intervals)

# counting the number of overlapping terms using a function.
noOfOveralppingTimes=NoOfOverlapping(input_intervals)

#function call to pop the overlapping terms from the given sequence
for i in range(noOfOveralppingTimes):
    output_intervals=PopIntervals(input_intervals)

#Printing the output sequence.
print("Output:", output_intervals)

"""
1)OP:
Input: [[1, 3], [2, 6], [6, 10], [10, 20], [20, 25]]
Output: [[1, 25]]

2)Input: [[1, 3], [2, 6], [8, 10], [15, 20], [16, 25]]
Output: [[1, 6], [8, 10], [15, 25]]

3)Input: [[1, 3], [2, 6], [6, 10], [15, 20], [16, 25]]
Output: [[1, 10], [15, 25]]
"""