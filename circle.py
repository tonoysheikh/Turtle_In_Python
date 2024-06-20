import turtle as t 
import random as rd

wn = t.Screen()
t.bgcolor("black")
t.pencolor("black")
t.pensize(1)
t.up()
t.goto(-150,0)
t.down()
for _ in range(1,11):
    rdcolor = (rd.random() , rd.random(),rd.random())
    t.fillcolor(rdcolor)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
    t.fd(30)
    t.down()

t.hideturtle()  
wn.exitonclick()