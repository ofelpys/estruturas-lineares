import math

class Bhaskara:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def delta(self) ->float:
        return self.b**2 - 4 * self.a * self.c
    
    def raizes(self) ->float:
        d = self.delta()
        if d < 0 :
            return "A raiz não existe"
        elif self.a == 0:
            return "Não é quação de segundo grau"
        elif d == 0:
            x =-self.b/(2*self.a)
            return "A raiz é: {:.2f}".format(x)
        else :
            x1 = (-self.b + math.sqrt(d))/ (2* self.a)
            x2 = (-self.b - math.sqrt(d))/ (2* self.a)
            return "A primeira raiz é {:.2f}, e a segunda é {:.2f}".format(x1,x2)