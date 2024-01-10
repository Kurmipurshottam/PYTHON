f = open('example 1.1.txt','r')

#as file ko read karta he

data = f.read()
print(data)

# 1 line me file fo read karta he -> f.readlines()

lines = f.readlines()
print("no of lines : ",len(lines))

# single 1 line ko read karta he

print(f.readline())