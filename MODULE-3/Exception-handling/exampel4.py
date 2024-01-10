'''
try : the code may have any problematic conditions goes inside this block

except : if try can not run successfully then this will run by default

else : if try will execute then this else also

finally : it will execute every time irrespective of any

'''

try:
    num=int(input("Enter num : "))
except:
    print("invalid input")
else:
    print(num*num)
finally:
    print("THANK YOU FOR USING THIS APPLICATION")