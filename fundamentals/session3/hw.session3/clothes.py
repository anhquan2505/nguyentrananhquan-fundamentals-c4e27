print("welcome to our shop, what do you want?")
a = str(input("choose: "))

s=["T-shirt", "sweaters"]
q=["c","r", "u", "d","exit"]   
def hàm(ls):
    strg = 'Your item: '
    for i in ls:
        strg = strg + i + "   "
    return (strg)
while True:
    if a in q:
        if a=="r": 
            print( hàm( s))
        elif a=="c":
            i=str(input("choose an item to add: "))
            s.append(i) 
            print( hàm( s))
        elif a=="u":
            b= (input("which one do you want to replace? (choose position of the item) "))
            while not b.isdigit():
                b = (input("which one do you want to replace? (choose position of the item) "))
            while int(b) not in range(1,len(s)+1):
                    print("nhập lại cmmd")
                    b = int(input("which one do you want to replace? (choose position of the item) "))   
            i=str(input("which one you want to add: "))
            s[int(b)-1] = i
            print( hàm( s))
        elif a == 'd':
            v= (input('Delete position ? : '))
            while not v.isdigit():
                v = (input("Delete position ? : "))
            while int(v) not in range(1,len(s)+1):
                print("nhập lại cmmd")
                v = int(input("Delete position ? : "))
            s.pop(int(v)-1)
            print( hàm( s))
        else  :
            break 
    else :
        print("sai cmm r, ngu vcl")
    
    a=str(input("m muốn cl j? đu ma mi(bấm exit để thoát)   "))  
    print()
    
