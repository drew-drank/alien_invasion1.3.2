import turtle
import math

__Pen = turtle.Pen()



a = 0.618
__Pen.speed(0)

__Pen.goto(-420,200)
c = __Pen.xcor()
__Pen.circle(a, extent=90)
__Pen.left(90)




b = __Pen.xcor() - c
for i in range(4):
    __Pen.forward(b)
    __Pen.left(90)
__Pen.left(315)


for i in range(16):
    
    __Pen.right(45)
    __Pen.circle(a, extent=90)
    __Pen.right(180)
    
    for i in range(4):
        __Pen.forward(b)
        __Pen.right(90)
    __Pen.right(135)
    a = (a / 0.618)
    b = (b / 0.618)

turtle.done()
