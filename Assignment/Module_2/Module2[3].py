'''
3 Differentiate between append () and extend () methods?
-> append() when we want to add a single item to the end of a list and extend()
     when we want to merge our list with another
'''
#example of append method
my_list = []
my_list.append(1)
print("append 1 in list = ",my_list)
# example of extend method
my_list = [5,6,7]
my_list.extend([1, 2, 3])
print("extend method = ",my_list)
