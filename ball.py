from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=0.4, stretch_len=0.5, outline=0)
        self.up()
        self.color("red")
        self.goto(x=-5,y=0)

        self.x = random.choice([1,-1])    # 1 - right, -1 - left
        self.y =  -1 # 1 - up, -1 - down
        self.speed = 0.4
        # self.heading = 45*5
        # self.body.setheading(self.heading+45*2*random.choice([0,1]))
    
    def move(self): 
        pos_x, pos_y = self.pos()
        self.goto(x=pos_x+0.4*20*self.x*self.speed, y = pos_y+0.4*20*self.y*self.speed)