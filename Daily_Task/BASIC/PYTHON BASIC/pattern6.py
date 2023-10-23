'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''
alphbet=65
for i in range(6):
    for j in range(i):
        print(chr(alphbet),end=" ")
        alphbet+=1
    print()
