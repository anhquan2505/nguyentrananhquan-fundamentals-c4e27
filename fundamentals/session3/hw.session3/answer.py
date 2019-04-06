form=['T-Shirt', 'Sweater']
def addon():
    new=input("enter new item: ")
    form.append(new)
    xuat()
def xuat():
    print("our items: ")
    for i in range(len(form)): print(i+1,".",form[i])
def update():
    x=int(input("update position: "))
    form[x-1]=input("enter new item: ")
    xuat()
def delet():
    x=int(input("delete position: "))
    form.pop(x-1)
    xuat()
ex=1
while(ex):
    y=input("Welcome to our shop, what do you want (C, R, U, D)?")
    y=y.upper()
    if(y=='R'): 
        xuat()
        print("type exit to exit")
    elif(y=='C'):
        addon()
        print("type exit to exit")
    elif(y=='U'):
        update()
        print("type exit to exit")
    elif(y=='D'):
        delet()
        print("type exit to exit")
    elif(y=='EXIT'):
        ex=0
    else:
        print("try again")