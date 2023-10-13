from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
    def create_paddle(self, position):
        self.shape("square")  # shape es un atributo que se puede inicializar al invocar a la clase
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)

         
    


