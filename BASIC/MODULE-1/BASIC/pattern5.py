'''
1   
2   3   
4   5   6   
7   8   9   10   
11   12   13   14   15   
'''
no=1
for i in range(6):
    for j in range(i):
        print(no,end="   ")
        no+=1
    print()
