import turtle
import time
import random
import json
import os

def load_high_scores(filename="high_scores.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_high_scores(scores, filename="high_scores.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4, ensure_ascii=False)

def get_player_name():
    return input('Введите nickname:')

def update_high_score(player_name, scores, filename="high_scores.json"):
    scores = load_high_scores(filename)
    if player_name not in scores or score>scores[player_name]:
        scores[player_name]= score
        save_high_scores(scores,filename)

player_name = get_player_name()
score = 0
high_scores = load_high_scores()
high_score = high_scores.get(player_name,0)

if high_scores:
    best_player = max(high_scores,key=high_scores.get)
    best_score = high_scores[best_player]
else:
    best_player = player_name
    best_score = high_score

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

wn.setup(width=1.0, height=1.0)
wn.tracer(0)


head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 470)

def update_score():
    pen.clear()
    pen.write(f'Игрок: {player_name} | Счет: {score} | Рекорд: {high_score} | Лидер: {best_player} ({best_score})', align='center', font=('Courier', 18, 'normal'))

def group():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []


while True:
    wn.update()
    if head.xcor() > 930  or head.xcor() < -930 or head.ycor()>500 or head.ycor() < -460:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        update_high_score(player_name, score)
        high_scores = load_high_scores()
        high_score = high_scores.get(player_name, 0)
        best_player = max(high_scores, key=high_scores.get)
        best_score = high_scores[best_player]
        score = 0
        update_score()
        delay = 0.1
    if head.distance(food) < 20:
        x = random.randint(-900, 900)
        y = random.randint(-400, 450)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        update_score()
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            update_high_score(player_name, score)
            high_scores = load_high_scores()
            high_score = high_scores.get(player_name, 0)
            best_player = max(high_scores, key=high_scores.get)
            best_score = high_scores[best_player]
            score = 0
            update_score()
            delay = 0.1
    time.sleep(delay)

wn.mainloop()