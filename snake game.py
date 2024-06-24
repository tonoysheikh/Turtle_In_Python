import turtle as t
import random as rd
import time

delay = 0.1

score = 0
high_score = 0

wn = t.Screen()
wn.title("Snake game")
wn.bgcolor("black")

wn.setup(width=800, height=500)
wn.tracer(0)

head = t.Turtle()
head.speed(0)
head.shape("turtle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = t.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

squareadd = []

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("cyan")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score : 0 High Score : 0" , align="center" , font=("Courier" , 20 , "normal"))

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right(): 
    if head.direction != "left":
        head.direction = "right"

def go_up(): 
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up": 
        head.direction = "down"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
wn.listen()   
wn.onkeypress(go_left , "a")
wn.onkeypress(go_right , "l")
wn.onkeypress(go_up , "f")
wn.onkeypress(go_down , "j")

while True:
    wn.update()
    
    if head.xcor() > 380 or head.xcor() < -380 or head.ycor() > 230 or head.ycor() < -230:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for i in squareadd:
            i.goto(1000,1000)
        
        squareadd.clear()

        score = 0
        
        delay = 0.1
        
        pen.clear()    
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center" , font=("Courier" , 20 , "normal"))
        
    if head.distance(food) < 20:
        x = rd.randint(-380 , 380)
        y = rd.randint(-230 , 230)
        food.goto(x,y)
        new_square = t.Turtle()
        new_square.speed(0)
        new_square.shape("square")
        new_square.color("green") 
        new_square.penup()
        squareadd.append(new_square)
        
        delay -= 0.001
        
        score += 10
        
        if score >= high_score:
            high_score = score
        
        pen.clear()    
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center" , font=("Courier" , 20 , "normal"))
    
    for i in range(len(squareadd)-1 , 0 , -1):
        x = squareadd[i-1].xcor()
        y = squareadd[i-1].ycor()
        squareadd[i].goto(x,y)
        
    if len(squareadd) > 0:
        x = head.xcor()
        y = head.ycor()
        squareadd[0].goto(x,y)
        
        
    move()
    
    for i in squareadd:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for i in squareadd:
                i.goto(1000,1000)
            
            squareadd.clear()
        
            score = 0
            
            delay = 0.1
            
            pen.clear()    
            pen.write("Score : {} High Score : {}".format(score, high_score), align="center" , font=("Courier" , 20 , "normal"))
    
    time.sleep(delay)
    
    
wn.mainloop()