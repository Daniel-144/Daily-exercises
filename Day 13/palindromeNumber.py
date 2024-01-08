"""
Problem #1
Input is a range of numbers as string. Print only the numbers that are palindromes and also the 
square of that number is also a palindrome.
eg. 121 is a palindrome and 121 * 121 = 14641 is also a palindrome, so you can print 121
131 is a palindrome, but 131*131 = 17161 is not a palindrome,so you can't print it.
eg input "10", "500"
Make sure to identify which steps need to be a function, how to avoid unnecessary parsing 
of numbers. Checking for palidrome or not, should be an efficient code.
"""
# function to check if the number is a pallindrome.
def pallindrome(number):
    # checking if the number is equal to the reversed format of the number
    if (number == number[::-1]):
        return True
    return False


seqOfNumber=input("enter the sequnce of the number (with spaces):").split(" ")
# list to store the list of the pallindrome number.
pallindromeList=[]
# loop to traverse through the list.
for number in seqOfNumber:
    # calling the function to check if the number is a pallindrome.
    if pallindrome(number)==True:
        # square the number to check if the square of number is also a pallindrome.
        num=str(int(number)**2)
        # if both conditions are satisfied then the number is appended in a list.
        if pallindrome(num) == True:
            pallindromeList.append(number)

print(f"the number which is a pallindrome and its square is also a pallindrome: {pallindromeList}")

"""
OP:
enter the sequnce of the number (with spaces):11 12 121 131 13
the number which is a pallindrome and its square is also a pallindrome: ['11', '121']
"""

