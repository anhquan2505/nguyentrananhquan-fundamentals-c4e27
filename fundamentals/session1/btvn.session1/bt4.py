from turtle import *
speed(2)
color("green", "yellow")


begin_fill()
for i in range (4):
    forward(100)                    
    left(90)
end_fill()
# hình 1


penup()
left(90)
forward(150)
pendown()

begin_fill()
circle(50)
end_fill()
# hình 2

penup()
right (90)
forward(100)
pendown()

begin_fill()
for i in range(3):
    forward(150)
    left(120)
end_fill()
# hình 3 

mainloop()