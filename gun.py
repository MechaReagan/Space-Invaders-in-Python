from turtle import Turtle
from bullet import Bullet


class Gun(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=1.5)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.alien_list = []
        self.bullet_list = []

    def go_to(self, x):
        x = x - 600
        self.goto(x, self.ycor())

    def shoot(self, bullet_list):
        if not bullet_list:
            bullet = Bullet(x=self.xcor(), y=-310)
            bullet_list.append(bullet)
            bullet.move()
        else:
            pass

    @staticmethod
    def check_hit(bullet_list, alien_list):
        for bullets in bullet_list:
            bullets.move()
            if bullets.ycor() > 420:
                bullets.hideturtle()
                bullets.clear()
                bullet_list.remove(bullets)
        for bullets in bullet_list:
            for alien in alien_list:
                if bullets.distance(alien) < 25:
                    alien.hideturtle()
                    alien.clear()
                    bullets.hideturtle()
                    bullets.clear()
                    bullet_list.remove(bullets)
                    alien_list.remove(alien)
                    return True

