from turtle import Turtle

class Points():
    def __init__(self) -> None:
        self.layers = []
        self.x = -185
        self.y = 267
        self.create_layers("red")
        self.create_layers("orange")
        self.create_layers("green")
        self.create_layers("yellow")
        

    def create_layers(self, color):
        for _ in range(2):
            layer = []
            for j in range(12):
                part = []
                for i in range(3):
                    part.append(Turtle(shape="square"))
                    part[-1].turtlesize(stretch_wid=0.4, stretch_len=0.5, outline=0)
                    part[-1].up()
                    part[-1].color(color)
                    part[-1].goto(x=self.x+0.4*20*i,y=self.y)
                self.x += 0.4*20*4
                layer.append(part)
            self.y -= 15
            self.x = -185
            self.layers.append(layer)

    # def point_collision_and_remove(self, ball):
    #     for layer in range(len(self.layers)):
    #         for part in range(len(self.layers[layer])):
    #             for item in self.layers[layer][part]:
    #                 if item.distance(ball) < 15:
                        
    #                     for _ in self.layers[layer][part]:
    #                         _.hideturtle()
    #                     self.layers[layer][part] = []
    #                     return True
    #     return False
    def point_collision_and_remove(self, ball):
        x = False
        for layer in range(len(self.layers)):
            for part in range(len(self.layers[layer])):
                for item in range(len(self.layers[layer][part])):
                    if self.layers[layer][part][item].distance(ball) < 15:
                        if self.layers[layer][part][1].distance(ball) < 20:
                            x = 'top'
                        else:
                            x = 'wall'
                        for _ in self.layers[layer][part]:
                            _.hideturtle()
                        self.layers[layer][part] = []
                        return x
        return x
