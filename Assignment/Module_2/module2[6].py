'''
6] Write a Python program to count the number of strings where the string length is 2 or more and
     the first and last character are same from a given list of strings.
'''
list1=['raj' , 'nikhiln' , 'purshottam' , 'smits']
count=0
#loop in list1
for word in list1:
    if len(word) > 1 and word[0] == word[-1]:
        count+=1
print("total string = ",count)


        
