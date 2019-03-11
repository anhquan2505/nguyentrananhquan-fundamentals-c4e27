from bt11 import is_inside
    
    
     
count = 0
for x in range(140,241):
    for y in range(60,261):
        
        if is_inside([x,y],[140,60,100,200]) == False:
            count +=1
            print(x,y)
if count != 0:
    print('your function has some f***ing problems')
else :
    print("just lucky, bitch")
