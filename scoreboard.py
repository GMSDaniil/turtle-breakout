from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(0, 320)
        self.color("white")
        self.write("Score: {}".format(self.score), move=False, align="center", font=("Courier", "18", "normal"))


    def game_over(self):
        self.clear()
        self.write("Game Over! Your score was: {}".format(self.score), move=False, align="center", font=("Courier", "20", "bold"))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score), move=False, align="center", font=("Courier", "18", "normal"))
        
    def win(self):
        self.clear()
        self.write("You won!".format(self.score), move=False, align="center", font=("Courier", "20", "bold"))