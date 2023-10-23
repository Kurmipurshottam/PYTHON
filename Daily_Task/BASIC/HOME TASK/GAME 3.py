#quiz questio enter in dictionary
quiz={}
dict1={}
a=1
for i in range(10):
    que=input(f'Enter your question no {a} : ')
    ans=input(f'Enter your answer no {a} : ') 
    quiz={que:ans}
    dict1.update(quiz)
print(dict1)
print("===========Game Start============")
score=0
b=1
for i in dict1:
    print(f'que : {b} :' ,i)
    ans_u=input("ans : ")
    b+=1
    if ans_u==dict1[i]:
        score+=5
        print('Score = ',score)
    else:
        score-=10
        print('Score = ',score)
print('your final score = ',score)

        
