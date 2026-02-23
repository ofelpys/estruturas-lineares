class Combustivel:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def consumo(self) ->float:
        return self.x/self.y