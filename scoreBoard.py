import turtle as t

ScoreBoardPos=(-50,250)
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(ScoreBoardPos)
        self.leftplayer=0
        self.rightplayer=0
        self.display_score()
    def update_score_leftplayer(self):
        self.leftplayer+=1
        self.display_score()
    def update_score_rightplayer(self):
        self.rightplayer+=1
        self.display_score()
    def display_score(self):
        self.clear()
        self.write(f"{self.leftplayer} | {self.rightplayer}",font=('Arial', 30, 'normal'))