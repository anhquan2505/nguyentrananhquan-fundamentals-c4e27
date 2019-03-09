

tron=[1,2,3,4]
question={1:{'if x=8, then what is the value of 4(x+3) ?':{1:44,2:35,3:36,4:40}},
2:{'if x=5, then what is the value of 3x(x+5)+4 ?':{1:154,2:353,3:236,4:140}},
3:{'Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? ':{1: 'About 55',2: 'About 65',3: 'About 75',4:'About 85'}}
}

for j in tron:
    print(question[j])
    
    

    answer=int(input('choose the answer: '))
    if answer == 1:
        print('just lucky')
    else :
        print("you're idiot")



