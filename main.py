from turtle import Screen, Turtle, getcanvas
from gun import Gun
from bullet import Bullet
from scoreboard import Scoreboard
from aliens import Aliens
import random

alien_list = []
bullet_list = []
enemy_bullets = []
gun_list = []
hit_value = 1

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Alien Invasion")
screen.tracer(0)
screen.addshape("alien.gif")

gun = Gun((0, -350))
gun_list.append(gun)

scoreboard = Scoreboard()


def fire():
    gun.shoot(bullet_list)


def alien_shoot(bullet_list, alien_list):
    global game_is_on
    for alien in alien_list:
        chance = random.randint(1, 5000)
        if chance == 1:
            bullet = Bullet(alien.xcor(), alien.ycor())
            bullet.y_move *= -1
            bullet.shape("arrow")
            bullet.setheading(270)
            bullet_list.append(bullet)
    for bullet in bullet_list:
        bullet.move()
        if bullet.ycor() < -420:
            bullet.hideturtle()
            bullet.clear()
            bullet_list.remove(bullet)
        if bullet.distance((gun.xcor(), gun.ycor())) < 25:
            bullet.hideturtle()
            bullet.clear()
            bullet_list.remove(bullet)
            if scoreboard.live_lost():
                game_is_on = False


screen.listen()
screen.onkey(fire, "space")


def motion(event):
        x = event.x
        gun.go_to(x)


canvas = getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
canvas.bind('<Motion>', motion)


Aliens.set_aliens(alien_list)
game_is_on = True
while game_is_on:
    screen.update()
    if gun.check_hit(alien_list=alien_list, bullet_list=bullet_list):
        scoreboard.score_point(hit_value)
    Aliens.move_aliens(alien_list)
    alien_shoot(bullet_list=enemy_bullets, alien_list=alien_list)
    gun_x, gun_y = gun.xcor(), gun.ycor()
    if Aliens.check_alien_collision(alien_list=alien_list, x=gun_x, y=gun_y):
        scoreboard.lives = 1
        scoreboard.live_lost()
        game_is_on = False
    if not alien_list:
        Aliens.set_aliens(alien_list)
        hit_value *= 2
        scoreboard.lives += 1
        scoreboard.update_scoreboard()



screen.exitonclick()