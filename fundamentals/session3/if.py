# y= int(input("năm sinh = "))
# x =  2019 - y
# if x <10: print("nhóc con")
# elif x<16: print("trẻ trâu")
# elif x> 150: print("chết đi cho đỡ tốn chỗ :)")
# else: print("già r đấy")

# x = input ("nhập năm sinh:")
# x.isdigit()
# a= 2019-int(x)
# print("tuổi của bạn là: ",a)
# LIST = [1, "foo", 3.5, { "hello": "bye" }]
# print( ", ".join( repr(e) for e in LIST ) )   

ls=["T-shirt","Sweater"]
while True:
    print("Welcom to our shop, what do you want")
    print("R: See all Item")
    print("C: Add new Item")
    print("U: Update Item")
    print("D: Delete Item")
    button=input("")
    if button == "R":
        print("Our Item: ",(ls))
    if button == "C":
        new=input("Enter new item: ")
        ls.append(new)
        print("Our Item: ",(ls))
    if button == "U":
        pos=int(input("Update position ?"))
        new=input("Enter new item: ")
        if pos<=len(ls):
            ls[pos-1]=new
        else:
            print("Your Position not exist !")
        print("Our Item: ",(ls))
    if button =="D":
        pos=int(input("Delete Position? "))
        if pos <=len(ls):
            ls.remove(ls[pos-1])
        else:
            print("Your Position not exist !")
        print("Our Item: ",(ls))