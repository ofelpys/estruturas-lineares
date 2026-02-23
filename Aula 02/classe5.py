class Salario:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def aumento(self) ->float:
        return self.x*(self.y/100)
    
    def novo_sal(self) ->float:
        return self.x+self.aumento()