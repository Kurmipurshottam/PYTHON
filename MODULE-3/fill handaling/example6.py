count=0
f=open("example3.txt","r")
d=f.read()
data=d.split()
for w in data:
    if not w.isnumeric():
        count+=1
        print(w)
print("total number of word = ",count)
