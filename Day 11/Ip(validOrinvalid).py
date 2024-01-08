"""
Problem #1
1. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
etc)
Write all constraints.
Get an input as string. Return if it is valid or not. 
Use string functions.
"""

def ValidIp(ip):
    # spliting the ip address into outlets.
    contents=ip.split(".")
    # conditional statement to check if they satisfy rule 1.
    if(len(contents) !=4):
        return False
    else:
        # loop to check if the outlets satisfy the condition 2 and condition 5.
        for content in contents:
            if(int(content)>255 or int(content)<0):
                return False
            if(len(content)>1 and content[0] == "0"):
                return False
    return True
        

"""
CONSTRAINS:
1) 4 numerical outlets seperated by periods (.).
2) Each octet should be a decimal number between 0 and 225
3) Length of the ip should be less than or equal to 15.
4) Ip address should not contain spaces.
5) outlets of the Ip address should not have a leading zeros.
"""

# enter a Ip address to check whether it is valid or not.
ipaddress=input("enter a ip address:")
# conditional statement to terminate exceptions of rule 3 and rule rule 4
if (len(ipaddress)>15 or (" " in ipaddress) ):
    print(f"entered ip address '{ipaddress} is not valid!!")
# else calling a function to check wheteher the given ip is valid or not.
else:
    if(ValidIp(ipaddress) == True):
        print(f"The given ip address '{ipaddress}' is valid!!")
    else:
        print(f"entered ip address '{ipaddress} is not valid!!")

"""
OP:
enter a ip address:0.0.0.0
The given ip address '0.0.0.0' is valid!!

enter a ip address:127.025.0.0
entered ip address '127.025.0.0 is not valid!!
"""