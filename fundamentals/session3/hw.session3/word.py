import random

print("WORD GAME")
print()
print("Rules: you have to correct words by arranging letters given below")
print("there are 4 level")

# lv=int(input("choose your level: "))


lv1=['apple','orange','grape']
lv2=['crab','fish','lobster']
lv3=['football','volleyball','parachuting']
lv4=['policeman','carpenter','firefighter']
# lv5=['psychology','diversity']
# lv6=['rhinoceros','elephant','megalodon']

while True:
    print('lv1 is about fruit. Just for warm up')
    for i in range(len(lv1)):
        
        q=list(lv1[i])
        random.shuffle(q)
        print(q)
        ans = str(input("answer: "))
        
        if ans == lv1[i]:
            print("right, but just very simple")
        else :
            print("wrong, idiot")
            
    quit=str(input("do you want to keep playing (yes or no)  "))
    if quit == "no":
        break
    else:
        print("        Turn to lv2, which is about sea animals")
        print()
        for i in range(len(lv2)):
            random.shuffle(q)
            q=list(lv2[i])
            random.shuffle(q)
            print(q)
            ans = str(input("answer: "))
            if ans == (lv2[i]):
                print("ok you are human")
            else:
                print("chicken")
        quit2=str(input("that's the end of lv2, do you want something harder? (yes or no): "))
        if quit2 == "no":
            break
        else :
            print('welcome to lv3 \n lv3 is about sports ')
            print()
            for i in range(len(lv3)):
                random.shuffle(q)
                q=list(lv3[i])
                random.shuffle(q)
                print(q)
                ans = str(input("answer: "))
                if ans == (lv3[i]):
                    print("good job")
                    print()
                else:
                    print("just a normal person")
                    print()
            quit3=str(input("that's the end of lv3, do you want the hardest? (yes or no): "))
            if quit3 == "no":
                break
            else:
                print('         welcome to the last level\n   there will be no clue now\n Good luck')
                for i in range(len(lv4)):
                    random.shuffle(q)
                    q=list(lv4[i])
                    random.shuffle(q)
                    print(q)
                    ans = str(input("answer: "))
                    if ans == (lv4[i]):
                        print("wow you are good")
                    else:
                        print("don't be upset")
                break
print('game over')




