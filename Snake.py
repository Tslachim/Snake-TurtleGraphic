from turtle import Turtle, Screen
import time
import random

skore = 0
hight_score = 0 

# Hlavní obrazovka
screen = Screen()
screen.bgcolor("yellow")
screen.title("Snake Game")
screen.setup(width= 600, height=600)
screen.tracer(False)

# Hadí hlava
head= Turtle("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.speed(0)
head.direction = "stop"

# Potrava
apple = Turtle("turtle")
apple.color("red")
apple.penup()
apple.speed(0)
apple.goto(random.choice(range(-280,280)),random.choice(range(-280,280)))

# Skóre
score = Turtle("square")
score.speed(0)
score.color("red")
score.penup()
score.hideturtle()
score.goto(0, 265)
score.write("Skóre: 0   Nejvyšší skóre: 0", align="center", font=("Arial", 18))

# Části těla
body_parts = []

# Funkce pohybu 
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

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Kliknutí na klávesy
screen.listen()
screen.onkeypress(move_up, "8")
screen.onkeypress(move_down, "5")
screen.onkeypress(move_left, "4")
screen.onkeypress(move_right, "6")


# Funkce pohybu


while True:
    screen.update()

    # Kontrola kolize s krajem obrazovky
    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1.3)
        head.goto(0, 0)
        head.direction = "stop"


        # Skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)
        
        # Vyprázdníme list s částmi těla 
        body_parts.clear()

        # Resetování skóre
        skore = 0
        score.clear()
        score.write(f"Skóre: {skore}  Nejvyšší skóre: {hight_score}", align="center", font=("Arial", 18))

    # vygenerování nové potravy (Kolize hlavy a potravy(jablka))
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        # Nová část těla (odsazení pod if = jen pokud sním potravu)
        new_body_part = Turtle("circle")
        new_body_part.speed(0)
        new_body_part.penup()
        new_body_part.color("blue")
        body_parts.append(new_body_part)

        # Zapsání skóre
        skore += 1

        if skore > hight_score:
            hight_score = skore

        score.clear()
        score.write(f"Skóre: {skore}   Nejvyšší skóre: {hight_score}", align="center", font=("Arial", 18))
    
    # Připojení zbylých kostiček za hlavu a první[nultý] díl.
    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)
    
    # Připojení první kostičky za hlavu hada
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)
    move()
    
    # Kontrola jestli hlava nenarazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(1.3)
            head.goto(0, 0)
            head.direction = "stop"

            # Skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)
                    
            # Vyprázdníme list s částmi těla 
            body_parts.clear()

            # Resetování skóre
            skore = 0
            score.clear()
            score.write(f"Skóre: {skore}  Nejvyšší skóre: {hight_score}", align="center", font=("Arial", 18))

    time.sleep(0.1)

screen.exitonclick()
