# nested dictionary
d1={
        'name':"raj",
        'fav_games':['cricket','hockey','football'],
        'subject':{'math':99,'science':98,'python':100}
        }
d2={
         'name':"raj",
         'fav_games':'cricket',
         'subject':'python'
        }
#for k in d2.items():access element of d2 
#print(k)
for k,v in d2.items():#access element of d2 in formet
    print(f' {k} = {v}')
#access element list as element of dictionary
print( 'fav_games in 1st index : ',d1['fav_games'][1])
#access element dictionary as element of dictionary
print('subjects of science mark : ',d1['subject']['science'])
