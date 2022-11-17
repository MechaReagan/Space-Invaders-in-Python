from turtle import Turtle
from bullet import Bullet
import random


class Aliens(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("alien.gif")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.value = 0
        self.x_move = .2
        self.y_move = -30
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    @staticmethod
    def set_aliens(alien_list):
        y = 250
        x = -535
        for _ in range(2):
            for _ in range(8):
                alien = Aliens((x, y))
                x += 90
                alien.value = 8
                alien_list.append(alien)
            y -= 60
            x = -535
        for _ in range(2):
            for _ in range(8):
                alien = Aliens((x, y))
                x += 90
                alien.value = 4
                alien_list.append(alien)
            y -= 60
            x = -535

    @staticmethod
    def move_aliens(alien_list):
        for aliens in alien_list:
            if (aliens.xcor() > 570) or (aliens.xcor() < -570):
                for aliens in alien_list:
                    aliens.move_down()
                    aliens.x_move *= -1
                break
        for aliens in alien_list:
            aliens.move()


    @staticmethod
    def check_alien_collision(alien_list, x, y):
        for alien in alien_list:
            if alien.distance((x, y)) < 35:
                return True
