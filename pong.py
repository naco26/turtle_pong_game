import turtle as t

SHAPESIZE_H = 1
SHAPESIZE_W = 3
class Pong(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(SHAPESIZE_W,SHAPESIZE_H)

    def position_Player(self,pos):
        self.penup()
        self.goto(pos)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)

    
