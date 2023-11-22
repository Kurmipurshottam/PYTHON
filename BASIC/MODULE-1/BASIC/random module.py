#random module
import random
li=[12,23,45,56]
#random number genrate from given range of integers
num=random.randint(1,100)
#genrate random element from collection
var=random.choice(li)
#will shuffel all the element in place
random.shuffle(li)
print("shuffel list = ",li)
print("random from list = ",var)
print("random from 1 to 100 = ",num)
