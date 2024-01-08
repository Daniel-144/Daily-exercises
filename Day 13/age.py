"""
Problem #2
Use switch stmt, think of all possible age as input.
Print if the user goes to kindergarten (age 3-6), primary school (7-11), ,middle school (12-15),
highschool (16-19), college (20-24).
Get users name and age as input.
Eg input Sam, 10
Output is Sam goes to primary school
"""
name=input("Enter your name:")
age=int(input("enter your age:"))

match age:
    case _ if age > 24:
        print(f"{name} is college passed out!!")
    case _ if age<=24 and age>=20:
        print(f"{name} goes to College")
    case _ if age<20 and age>=16:
        print(f"{name} goes to High School")
    case _ if age<16 and age>=12:
        print(f"{name} goes to Middle School")
    case _ if age<12 and age>=7:
        print(f"{name} goes to Primary school")
    case _ if age<7 and age>=3:
        print(f"{name} goes to Kindergarten")
    case _:
        print("invalid Input!!") 

"""
OP:
Enter your name:sam 
enter your age:10 
sam goes to Primary school
"""
