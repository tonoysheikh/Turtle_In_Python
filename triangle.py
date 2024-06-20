import turtle as t

wn = t.Screen()
t.bgcolor("black")
t.pencolor("white")
t.fillcolor("orange")

t.begin_fill()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()

t.up()
t.right(60)
t.forward(70)

t.down()
t.fillcolor("green")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(-120)
    
t.end_fill()
t.hideturtle()
wn.exitonclick()