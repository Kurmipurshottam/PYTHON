'''
19] Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''
string1=input("Enter the string = ")
n_str=string1.find("not")
p_str=string1.find("poor")
if (n_str>=0 and p_str>=0):
    string1=string1.replace(string1[n_str:p_str+4],"good")
print("string = ",string1)
