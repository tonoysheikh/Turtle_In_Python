import turtle as t

wn = t.Screen()
wn.bgcolor("black")

t.pencolor("white")

t.fillcolor("red")

t.begin_fill()
t.left(140)
t.forward(160)
t.circle(-80, 200)

t.left(120)
t.circle(-80, 200)
t.forward(160)

t.end_fill()

t.hideturtle()
wn.exitonclick()
