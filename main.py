import turtle as t
from pong import Pong
from ball import Ball
from scoreBoard import ScoreBoard
import time


torry = t.Turtle()
screen = t.Screen()
POSITIONS = [(-370,0),(350,0)]
BGCOLOR = "black"
WIDTH = 800
HEIGHT =600
TOP_BOTTOM_COLISSION_CHECK=280
## Screen Attributes
screen.title("PONG GAME 2023")
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor(BGCOLOR)
screen.tracer(0)
screen.listen()

# 2 Pong for Players
right_paddle = Pong()
right_paddle.position_Player(POSITIONS[1])
left_paddle = Pong()
left_paddle.position_Player(POSITIONS[0])

#Ball for the Game
b = Ball()

#score board
ScoreB = ScoreBoard()
GameOver = t.Turtle()
GameOver.hideturtle()
GameOver.color("white")
GameOver.penup()

screen.onkey(key="Up",fun=right_paddle.move_up)
screen.onkey(key="Down",fun=right_paddle.move_down)
screen.onkey(key="w",fun=left_paddle.move_up)
screen.onkey(key="s",fun=left_paddle.move_down)



is_game_on=True

GameOver.write("Good Luck!!",align="center",font=('Arial', 35, 'normal'))
GameOver.clear()
time.sleep(0.3)
while is_game_on:
    screen.update()
    b.move_ball()
    time.sleep(b.ball_speed)

    #Detect collision with top and bottom walls
    if b.ycor()>TOP_BOTTOM_COLISSION_CHECK or b.ycor()<-TOP_BOTTOM_COLISSION_CHECK:
        b.bounce_from_walls()

    #Detect bouncing by players
    if (b.xcor()>320 or b.xcor()<-340) and (b.distance(right_paddle) <50 or b.distance(left_paddle)<50):
        b.bounce_from_paddle()

    #Update score and refresh ball position if balls crosses the right paddle
    if(b.xcor()>350):
        ScoreB.update_score_leftplayer()
        b.refresh()

    #Update score and refresh ball position if balls crosses the left paddle
    if(b.xcor()<-360):
        ScoreB.update_score_rightplayer()
        b.refresh()

    if(ScoreB.leftplayer>=10 or ScoreB.rightplayer>=10):
        winner = "Left" if (ScoreB.leftplayer>ScoreB.rightplayer) else "Right"
        is_game_on=False
        GameOver.write(f" {winner} won!!",align="center",font=('Arial', 35, 'normal'))


screen.exitonclick()