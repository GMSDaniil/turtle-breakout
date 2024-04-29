from turtle import Turtle

class Layout():
    def __init__(self) -> None:
        self.col1 = []
        self.row = []
        self.col2 = []
        self.create_layout()
    
    def create_layout(self):
        for i in range(80):
            self.col1.append(Turtle(shape="square"))
            self.col1[-1].turtlesize(stretch_wid=0.4, stretch_len=0.4, outline=0)
            self.col1[-1].color("white")
            self.col1[-1].up()
            self.col1[-1].goto(x=-200, y=-350+0.4*20*i)

            self.col2.append(Turtle(shape="square"))
            self.col2[-1].turtlesize(stretch_wid=0.4, stretch_len=0.4, outline=0)
            self.col2[-1].color("white")
            self.col2[-1].up()
            self.col2[-1].goto(x=200, y=-350+0.4*20*i)

        for i in range(50):
            self.row.append(Turtle(shape="square"))
            self.row[-1].turtlesize(stretch_wid=0.4, stretch_len=0.4, outline=0)
            self.row[-1].color("white")
            self.row[-1].up()
            self.row[-1].goto(x=-200+0.4*20*i, y=282)
    

    def wall_collision(self, ball):
        for part in self.col1:
            if part.distance(ball) < 13:
                return True
        
        for part in self.col2:
            if part.distance(ball) < 13:
                return True
        return False
    
    def roof_collision(self, ball):
        for part in self.row:
            if part.distance(ball) < 13:
                return True
        return False

        