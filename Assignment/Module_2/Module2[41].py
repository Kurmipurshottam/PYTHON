'''
40] Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

'''
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print("dictionary 1 = ",d1)
print("dictionary 2 = ",d2)
combine_dict = {}
# Combine dictionaries, adding values for common keys
for i in d1:
    if i in d2:
        combine_dict[i] = d1[i] + d2[i]
    else:
        combine_dict[i] = d1[i]
# Add values from d2 for keys not in d1
    for i in d2:
        if i not in d1:
            combine_dict[i] = d2[i]
print("combine two dictionary adding value for common key = ",combine_dict)

