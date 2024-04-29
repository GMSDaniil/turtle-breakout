from turtle import Screen
from layout import Layout
from board import Board
from scoreboard import Scoreboard
from ball import Ball
from points import Points
import time
import random
import datetime
from playsound import playsound

screen = Screen()
screen.setup(width=500, height=700)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

layout = Layout()
board = Board()
ball = Ball()
scoreboard = Scoreboard()
points = Points()

screen.listen()


def start():
    game_is_on = True
    screen.onclick(None)
    screen.onkey(board.left, "Left")
    screen.onkey(board.right, "Right")
    global forget
    forget = 0
    while game_is_on:
        screen.update()
        time.sleep(0.01)
        ball.move()
        
        ##using forget variable to avoid sticking ball to the wall/board

        ###ball wall colision
        if (layout.wall_collision(ball) and not forget) or (layout.wall_collision(ball) and (datetime.datetime.now()-forget_time).total_seconds() > 0.1):
            playsound('sounds/wall.mp3', block=False)
            ball.x *= -1
            forget = 1
            forget_time = datetime.datetime.now()

        ###roof collision
        if (layout.roof_collision(ball) and not forget) or (layout.roof_collision(ball) and (datetime.datetime.now()-forget_time).total_seconds() > 0.1):
            playsound('sounds/wall.mp3', block=False)
            ball.y *= -1
            forget = 1
            forget_time = datetime.datetime.now()

        ###board collision
        if (board.ball_collision(ball) and not forget) or (board.ball_collision(ball) and (datetime.datetime.now()-forget_time).total_seconds() > 0.1):
            playsound('sounds/board.mp3', block=False)
            ball.y *= -1
            ball.x *= random.choice([1,-1])
            forget = 1
            forget_time = datetime.datetime.now()


        ###point collision:  remove point, add score, add speed, change direction
        x = points.point_collision_and_remove(ball)
        if x != False:
            playsound('sounds/score.mp3', block=False)
            scoreboard.refresh()
            ball.speed += 0.005
            if x == 'wall':
                ball.x *= -1
            else:
                ball.y *= -1
                
        ###Win
        if scoreboard.score == 84:
            playsound('sounds/win.mp3', block=False)
            scoreboard.win()
            return

        ####game over
        if ball.ycor() < -350:
            playsound('sounds/lose.mp3', block=False)
            scoreboard.game_over()
            return
        

screen.onkey(start, "Left")
screen.onkey(start, "Right")


screen.update()

screen.mainloop()


    