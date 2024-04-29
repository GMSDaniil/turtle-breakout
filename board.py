from turtle import Turtle

class Board():
    def __init__(self) -> None:
        self.parts = []
        self.create_board()
    
    def create_board(self):
        for i in range(4):
            self.parts.append(Turtle(shape="square"))
            self.parts[-1].turtlesize(stretch_wid=0.4, stretch_len=0.5, outline=0)
            self.parts[-1].color("blue")
            self.parts[-1].up()
            self.parts[-1].goto(x=-20+0.4*20*i, y=-300)
    
    def right(self):
        if self.parts[-1].pos()[0]+30 > 190:
            for part in range(len(self.parts)):
                self.parts[part].goto(x=160-0.4*20*3+0.4*20*part, y=-300)

        for part in range(len(self.parts)):
            self.parts[part].forward(30)

    def left(self):
        if self.parts[0].pos()[0]-30 < -190:
            for part in range(len(self.parts)):
                self.parts[part].goto(x=-160+0.4*20*3-0.4*20*part, y=-300)

        for part in range(len(self.parts)):
            self.parts[part].forward(-30)

    
    def ball_collision(self, ball):
        for part in self.parts:
            if part.distance(ball) < 13:
                return True
        return False

    