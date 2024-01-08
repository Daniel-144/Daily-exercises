"""
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
"""

def CalculateOp(sequence):
    operatorList=[]
    operandList=[]
    op=None
    for char in sequence:
        if char.isdigit():
            operandList.append(int(char))
        else:
            operatorList.append(char)
        if len(operatorList) >=1 and len(operandList) >=2:
            operand1=operandList.pop()
            operand2=operandList.pop()
            operator=operatorList.pop()
            if operator == "+":
                operandList.append(operand1+operand2)
            elif operator == "-":
                operandList.append(operand1-operand2)
            elif operator == "/":
                operandList.append(operand1/operand2)
            elif operator == "*":
                operandList.append(operand1*operand2)
            else:
                return ("the sequence contains invalid character!!")
    op=operandList[0]
    return(op)

            

inputSequence=input("Enter a sequence of mixed expressions example(+ 1 2 * 5):")
inputSequence=inputSequence.split(" ")
#inputSequence=["+","1", "2", "*", "5"]
output=CalculateOp(inputSequence)
print(f"The output of the sequence is: {output}")

