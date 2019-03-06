from turtle import * 

y= ["red", "blue", "brown", "yellow","grey"]
a=[120,90,72,60,360/7]
for i in range(5):
    color(y[i])
    for j in range(1,i+4):
        forward(100)
        left(a[i])

right(90)
color("white")
forward(100)
left(90)

for i in range (5):
    color(y[i])
    begin_fill()
    
    for j in range(4):
        if j%2 !=0: forward(100)
        else : forward(50)
        right(90)
    forward(50)

    end_fill()
mainloop()
