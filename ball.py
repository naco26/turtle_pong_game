import turtle as t

BALL_SIZE_W = 0.7
BALL_SIZE_H = 0.7
BALL_POS = (-10,0)

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.xmove=10
        self.ymove=10
        self.shapesize(BALL_SIZE_W,BALL_SIZE_H)
        self.penup()
        self.goto(BALL_POS)
        self.move_ball()
        self.ball_speed=0.1
    
    def move_ball(self):
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)

    def bounce_from_walls(self):
        self.ymove*=-1

    def bounce_from_paddle(self):
        self.xmove*=-1
        self.ball_speed*=0.9

    def refresh(self):
        self.goto(BALL_POS)
        self.xmove*=-1
        self.ball_speed=0.1

        