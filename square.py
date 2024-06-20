import turtle as t
import random as rd

wn = t.Screen()
t.setup(800 , 500)
t.bgcolor("black")
t.pencolor("white")

t.up()
t.lt(180)
t.fd(350)
t.down()

for i in range(1,6):
    rdcolor = (rd.random() , rd.random() , rd.random())
    t.fillcolor(rdcolor)
    t.begin_fill()
    for _ in range(1,5):
        t.bk(100)
        t.lt(90)
    t.end_fill()
    t.up()
    t.bk(150)
    t.down()
   
t.hideturtle()
wn.exitonclick()