import math

class Triangulo:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def hip(self) ->float:
        return math.sqrt(self.x*2+self.y*2)