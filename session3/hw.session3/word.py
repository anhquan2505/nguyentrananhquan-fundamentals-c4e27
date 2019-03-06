import random

print("WORD GAME")
print()
print("Rules: you have to correct words by arranging letters given below")
# print("there are 2 level")

# lv=int(input("choose your level: "))


lv1=['apple','orange','grape']
lv2=['crab','fish','lobster']
# lv3=['football','volleyball','parachuting']
# lv4=['policeman','carpenter','firefighter']
# lv5=['psychology','diversity']
# lv6=['rhinoceros','elephant','megalodon']
# for i in range(len(lv2)):
#         q=list(lv2[i])

#         random.shuffle(q)
#         print(q)
#         ans = str(input("answer: "))

for i in range(len(lv1)):
    q=list(lv1[i])

    random.shuffle(q)
    print(q)
    ans = str(input("answer: "))
    if ans == (lv1[i]):
        print("right, but just very simple")
    else:
        print("wrong, idiot")


for i in range(len(lv2)):
    q=list(lv2[i])

    random.shuffle(q)
    print(q)
    ans = str(input("answer: "))
    if ans == (lv2[i]):
        print("ok you are human")
    else:
        print("chicken")


    





