def say_hi():
    print('hi')
    print('bye')
say_hi()

# def add_two_number4(a,b):
    
#     print('tong 2 so la', a+b)
# num1= int(input('nhap so thu nhat: '))
# num2=int(input('nhap so thu hai: '))
# add_two_number4(num1,num2)


# def add_two_number(a,b):
#     return(a+b)
# num1= int(input('nhap so thu nhat: '))
# num2=int(input('nhap so thu hai: '))
# num3=int(input('nhap so thu ba: '))
# sum_1_2=add_two_number(num1,num2)
# sum_3=add_two_number(sum_1_2,num3)
# print('tong 3 so ',sum_3)

# # lenh return phai nam trong body cua ham
# # lenh return se tra ve ket qua cho loi goi ham
# # trong ham co the k co, co 1 hoac nhieu lenh return
# # # khi gap lenh return thi cac cau lenh sau do se k dc thuc hien nx

# # def abs_of_number(a):
# #     if a>0: 
        
# #         print('tri tuyet doi la ',a)
# #         return(a)
# #     else:
        
# #         print('tri tuyet doi la',-a)
# #         return -a
# #     print('tri tuyet doi la',a)
# # x= abs_of_number(-12)
# # tong=12+ abs_of_number(-12)  
# # print(x,'  ', tong) 


# def evaluate(a,b,x):
#     if x == '+':
#         return(a+b)
#     elif x=='*':
#         return(a*b)
#     elif x=='/':
#         return(a/b)
#     else :
#         return(a-b)
# a=int(input('nhap so thu 1: '))
# b=int(input('nhap so thu 2: '))
# x=str(input('nhap phep toan: '))
# print('dap an cua phep tinh do la: ',evaluate(a,b,x))

# def evaluate1(a,b,x):
#     return eval(a+x+b)
# q=str(input('so thu nhat: '))
# w=str(input('so thu hai : '))
# e=str(input('dau'))
# print(evaluate1(q,w,e))

def nguyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return(False)
            
    return(True)
            
n = int(input('nhap so can ktra: '))
for v in range(2,n+1):
    if nguyento(v):
        print('cac so nguyen to nho hon ',n,'la: ',v)
# if nguyento(n):
#     print('dp la so ngto')
# else :
#     print('la so ngto')
