from  turtle import *
speed(0)
def draw_square(a,b):
    color(b)
    for j in range(4):
        forward(a)
        left(90)
    


for i in range(50):
    draw_square(i * 4, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()