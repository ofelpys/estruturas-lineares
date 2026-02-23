##AULA 02
##Exercício 02
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe2 import Funcao

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 02<<<<<<<<<<<<<<<<<<<<<<\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>Cálculo Média<<<<<<<<<<<<<<<<<<<<<<\n")

    x = float(input("Digite o valor de x para saber o valor dele na seguinte função y = (3*x) +2: "))

    calc = Funcao(x)

    print(f"A valor de y(x) = {calc.funcao()}")


if __name__ == "__main__":
    main()