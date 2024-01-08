"""
Problem #3
Use switch stmt (no if stmts) to calculate the grade of the student based on marks
Grade A = mark >90
Grade B  between 80 and 90
Grade C between 60 and 80
Fail , below 60

Make sure to include code for all possible input values.
"""
def grade(mark):
    match (mark):
        case _ if 100 >= mark >90:
            return "Grade A"
        case _ if 80 <= mark <= 90:
            return "Grade B"
        case _ if 60 >= mark <=79:
            return "Grade C"
        case _ if 60 > mark <=0:
            return "FAIL"
        case _:
            return "Invalid Input"

mark=int(input("Enter your mark:"))
print(f"OUTPUT:{grade(mark)}")

"""
OP:
1)Enter your mark:100
OUTPUT:Grade A

2)Enter your mark:90
OUTPUT:Grade B

3)Enter your mark:101
OUTPUT:Invalid Input
"""
    
