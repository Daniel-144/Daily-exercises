"""
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15
"""
def CalculateOP(inputsequence):
    # initializing a list to store values.
    Oplist=[]
    # loop to iterate through the list.
    for char in inputSequence:
        # checking if the element is a digit.
        if char.isdigit():
            Oplist.append(int(char))
        # if it is not a digit then check if it is a operator
        else:
            if char == "*":
                # storing the character which is poped from the list in operand 1 
                operand1=Oplist.pop()
                # storing the character which is poped from the list in operand 2
                operand2=Oplist.pop()
                # append the product of the 2 operands in the list.
                Oplist.append(operand1*operand2)
            elif char == "-":
                # storing the character which is poped from the list in operand 1 
                operand1=Oplist.pop()
                # storing the character which is poped from the list in operand 2
                operand2=Oplist.pop()
                # append the difference in the list.
                Oplist.append(operand2-operand1)
            elif char == "+":
                # storing the character which is poped from the list in operand 1 
                operand1=Oplist.pop()
                # storing the character which is poped from the list in operand 2
                operand2=Oplist.pop()
                # append the sum of the 2 numbers in tghe list.
                Oplist.append(operand1+operand2)
            elif char == "/":
                # storing the character which is poped from the list in operand 1 
                operand1=Oplist.pop()
                # storing the character which is poped from the list in operand 2
                operand2=Oplist.pop()
                # append the quotient obtained by dividing the 2 numbers in the list
                Oplist.append(round(operand1/operand2,2))
            # if it is not the 4 operands it may be a invalid value.
            else:
                return("the input has invalid characters!!!")
    return(Oplist[0])

# input sequence.
inputSequence=input("enter a expression with combination of numbers and operatos with spaces:")
inputSequence=inputSequence.split(" ")
#inputSequence=["10", "2", "3", "+","-", "5", "*"]
# calling the function to calculate the output.
output=CalculateOP(inputSequence)
print(f"Input: {inputSequence}")
# print the output.
print(f"Output:{output}")

"""
1)Input: ['1', '2', '+', '5', '*']
Output:15

2)Input: ['10', '2', '3', '+', '-', '5', '*']
Output:25
"""