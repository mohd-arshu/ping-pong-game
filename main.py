from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# ////////////////////////////////////////

rpaddle = Paddle((350, 0))   
screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")

# /////////////////////////////////////////////


lpaddle = Paddle((-350, 0))
screen.listen()
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320:
        ball.x_move *= -1

    if ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.x_move *= -1


    if ball.xcor() > 380 : 
        ball.goto(0, 0)
        ball.x_move *= -1
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.x_move *= -1
        scoreboard.l_point()
        

    

screen.exitonclick()