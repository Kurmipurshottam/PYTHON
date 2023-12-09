# 40]  Write a Python program to map two lists into a dictionary.
list1=[1,2,3,4]
list2=['raj','smith','nikhil','purshottam']
print("list1 = ",list1)
print("list2 = ",list2)
map_dictionary={}
if len(list1)==len(list2):
    for i in range(len(list1)):
        map_dictionary[list1[i]]=list2[i]
print("after mapping two list = ",map_dictionary)
