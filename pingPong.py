import turtle
import time

# Screen
sc = turtle.Screen()
sc.title("Ping Pong")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Scoring
left_player = 0
right_player = 0

# Display the Score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player 1: 0   Player 2: 0",
    align="center", font=("Courier", 20, "bold"))

# Move paddles
def paddle1up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
        left_paddle.sety(y)

def paddle1down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
        left_paddle.sety(y)

def paddle2up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
        right_paddle.sety(y)

def paddle2down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 20
        right_paddle.sety(y)


#Key Bindings
sc.listen()
sc.onkeypress(paddle1up, "w")
sc.onkeypress(paddle1down, "s")
sc.onkeypress(paddle2up, "Up")
sc.onkeypress(paddle2down, "Down")

# Main Game Loop
while True:
    sc.update()
    time.sleep(0.01)

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    #Check Borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
    
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Player 1: {}   Player 2: {}".format(
            left_player, right_player), align="center", 
            font=("Courier", 24, "bold"))
    
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Player 1: {}   Player 2: {}".format(
            left_player, right_player), align="center", 
            font=("Courier", 24, "bold"))

    # Collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and \
            (hit_ball.ycor() < right_paddle.ycor() + 50 and hit_ball.ycor() > right_paddle.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and \
            (hit_ball.ycor() < left_paddle.ycor() + 50 and hit_ball.ycor() > left_paddle.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1