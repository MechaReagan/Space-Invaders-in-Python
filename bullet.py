from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move = 1
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.move_speed = 0.05
        self.setx(x)
        self.sety(y)

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)


