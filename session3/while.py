# y = input(" nhập năm sinh:")

# while not y.isdigit():
#     print("bạn nhập sai rồi mời nhập lại:")
#     y= input("nhập năm sinh:")
# x = 2019 - int(y)
# print("tuổi của bạn là:", x)

    # while: làm đến khi nào đùng thì thôi 

from turtle import *
speed()
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    # if abs(pos()) < 1:
    #     break
end_fill()
done()