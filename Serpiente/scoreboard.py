from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=260)
        self.score_text()
    def score_text(self):
        self.clear()
        self.write(f"Score:  {self.score_num} ", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        
        self.score_num += 1
        self.score_text()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game over", align=ALIGNMENT, font=FONT)




