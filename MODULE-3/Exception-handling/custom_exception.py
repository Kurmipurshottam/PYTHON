'''
there are two types of exception
1] built in exception
2] user definr exception
-> it is create by the user and we can call as per the requirement.
'''
class myexception(Exception):
    pass
try:
    num = int(input("Enter a number = "))
    if num<0:
        raise myexception    
except myexception:
    print("number must be positive")