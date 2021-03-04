import math

def exceed_capacity(s,r):
    if  s > 200:
        print("Warning: Total number of customer exceeds the room capacity. Ignoring "+r+" and all the requests after")
        return True
    return False

def is_valid_amount(n,r):
    if n <= 0 or n >=20:
        print("Warning: "+r+" gives invalid number of people. Ignoring this request")
        return False
    return True
