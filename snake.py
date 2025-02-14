import turtle
import random
import time

score = 0
delay = 0
high_score = 0

w = turtle.Screen() # window
w.bgcolor('green')
w.title('snake game')
w.tracer(1)
w.setup(width=1.0,height=1.0)

head = turtle.Turtle()
head.shape("square")
head.color("black")
head.goto(0,0)
head.penup()
head.direction='Stop'

food = turtle.Turtle()
food.shape('square')
food.color('red')
food.speed(0)
food.penup()
food.goto(random.randint(-400,400),random.randint(-400,400)) # except 0!!!

p = turtle.Turtle()
p.speed(0)
p.shape('square')
p.color('white')
p.penup()
p.hideturtle()
p.goto(0,480)
p.write('Score:0 High Score:0', align='center', font=('verdana',20, 'bold'))


def up():
    if head.direction != 'down':
        head.direction = 'up'

def down():
    if head.direction != 'up':
        head.direction = 'down'

def left():
    if head.direction != 'right':
        head.direction = 'left'

def right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+10)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-10)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+10)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-10)

w.listen()
w.onkeypress(up,'w')
w.onkeypress(down,'s')
w.onkeypress(left,'a')
w.onkeypress(right,'d')

segments = []

while True:
    w.update()
    if head.xcor() > 960  or head.xcor() < -960 or head.ycor()>540 or head.ycor() < -520:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'Stop'
        
    turtle.exitonclick()

