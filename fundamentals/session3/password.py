# mk= input("mời bạn nhập mk: ")
# while True:
#     if len(mk)>8:
#         break
#     print(" mk k đủ ký tự")
#     mk= input("mời bạn nhập lại mk: ")
    

# print("ting ting")

# loop_count = 0
# while True:
#     print("loop count: ", loop_count)
#     # loop_count-=1
#     loop_count=loop_count+1
#     # <=> loop_count + =1
#     if loop_count>=3:
#         break
# print("abc")

# nhập 3 hệ số a b c để giải pt bậc 2
# a =(input(" nhập hệ số a= "))
# while not a.isdigit():
#     print("mời nhập lại a")
#     a =(input(" nhập hệ số a= "))
    
# a = int(a)
# b =(input("nhập hệ số b= "))
# while not b.isdigit() :
#     print("mời nhập lại b")
#     b =(input("nhập hệ số b= "))
    
# b = int(b)
# c = (input("nhập hệ số c= "))   
# while not c.isdigit():   
#     print("mời nhập lại c")
#     c = (input("nhập hệ số c= "))
# c = int(c)
    
# # a*(x**2)+ b*x+c=0
# y=float(b**2 - 4*a*c)
# if a>0:
#     if b**2 - 4*a*c > 0:
#         x=float((-b+y**0.5)/(2*a))
#         print(x)
#         z=float((-b-y**0.5)/(2*a))
#         print(z)
#     elif b**2 - 4*a*c == 0:
#         x=float(-b/(2*a))
#         print(x)
#     else :
#         print("không có nghiệm")
# else :
#     print("không phải pt bậc 2")
ls = []
n= int(input("moi ban nhap so phan tu"))
for i in range (n):
    print("nhap phan tu thu :",i+1)
    so=int(input(""))
    ls.append(so)
print("day ban vua nhap la")
print(ls)

print("tong day vua nhap ")
print(sum(ls))

print("phan tu thu 2 trong day")
print(ls[1])