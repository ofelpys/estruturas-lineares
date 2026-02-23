##AULA 02
##Exercício 06
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe6 import Triangulo

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 06<<<<<<<<<<<<<<<<<<<<<<\n")

    x = float(input("Digite o cateto Oposto do angulo:\n"))
    y = float(input("Digite o cateto adjacente do angulo:\n"))

    calc = Triangulo(x,y)

    print("O cateto oposto é: {:.2f}".format(x))
    print("O cateto adjacente é: {:.2f}".format(y))
    print("O resultado da hipotenusa é: {:.2f}".format(calc.hip()))

    print
if __name__ == "__main__":
    main()