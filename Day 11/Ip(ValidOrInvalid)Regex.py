import re

def ValidIp(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Check if the it matches the pattern
    if re.match(pattern, ip):
        # spliting the ip address into outlets.
        contents=ip.split(".")
        # loop to check if the outlets satisfy the condition 2 and condition 5.
        for content in contents:
            if(int(content)>255 or int(content)<0):
                return False
            if(len(content)>1 and content[0] == "0"):
                    return False
            return True
        else:
            return False
        


IpAddress = input("enter any ip address:")
# conditional statement to terminate exceptions of rule 3 and rule rule 4
if (len(IpAddress)>15 or (" " in IpAddress) ):
    print(f"entered ip address '{IpAddress} is not valid!!")
# else calling a function to check wheteher the given ip is valid or not.
else:
    if(ValidIp(IpAddress) == True):
        print(f"The given ip address '{IpAddress}' is valid!!")
    else:
        print(f"entered ip address '{IpAddress} is not valid!!")