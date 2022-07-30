# drawing a square sheet

import turtle
t = turtle.Turtle()
t.speed(10)

for i in range(0,400,20):
    t.pencolor('lightgrey')
    t.penup()
    t.setpos(-200+i,-200)
    if i == 0:
        t.left(90)
    t.pendown()
    t.forward(400)
    t.backward(400)
for i in range(0,400,20):
    t.pencolor('lightgrey')
    t.penup()
    t.setpos(-200,-200+i)
    if i == 0:
        t.right(90)
    t.pendown()
    t.forward(400)
    t.backward(400)
t.penup()