import random
li=[]
user_li=[]
computer_li=[]
computer_count=0
user_count=0
#taking input from user how many element do you want to enter
n=int(input("how many element you want to enter in list = "))
for i in range(n):
    no=int(input("enter element = "))
    li.append(no)
print("main list : :",li)
#main list divided using lisst length
u1=int(len(li)/2)
#main list is divided and some element append in user_list
for i in range(u1):
    user_li.append(li[i])
print("user list : :",user_li)
#reamain element in main list append in computer_list
for i in li:
    if i not in user_li:
        computer_li.append(i)
print("computer list : :",computer_li)
#game logic
#taking random choice from main list
for i in range(n):
    random_choice=random.choice(li)
    print("random choice = ",random_choice)
    if random_choice in user_li:
        user_li.remove(random_choice)
        user_count+=1
        print("updated user list = ",user_li)
        print("updated computer list = ",computer_li)
        print("user score = ",user_count)
        print("computer score = ",computer_count)
    elif random_choice in computer_li:
        computer_li.remove(random_choice)
        computer_count+=1
        print("updated user list = ",user_li)
        print("updated computer list = ",computer_li)
        print("user score = ",user_count)
        print("computer score = ",computer_count)
    li.remove(random_choice)
    if computer_count==5:
        print(": : computer is winner : :")
        break
    elif user_count==5:
        print(": : user is winner: :")
        break
    i+=1
#finish
