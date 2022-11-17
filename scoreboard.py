from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-400, 300)
        self.write(f"Lives:{self.lives}", align="center", font=("Courier", 60, "normal"))
        self.goto(350, 300)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 60, "normal"))

    def live_lost(self):
        self.lives -= 1
        self.update_scoreboard()
        if self.lives == 0:
            self.goto(0, -200)
            self.color("red")
            self.write(f"GAME OVER", align="center", font=("Courier", 100, "normal"))
            return True

    def score_point(self, value):
        self.score += value
        self.update_scoreboard()