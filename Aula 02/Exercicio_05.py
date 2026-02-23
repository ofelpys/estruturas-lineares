##AULA 02
##Exercício 05
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe5 import Salario

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 05<<<<<<<<<<<<<<<<<<<<<<\n")

    x = float(input("Entre com seu salário:\n"))
    y = float(input("Entre com o percentual de aumento:\n"))

    calc = Salario(x,y)

    print("O salário é: {:.2f}".format(x))
    print("O aumento é de {:.2f}".format(calc.aumento()))
    print("O novo salário é: R${:.2f}".format(calc.novo_sal()))


if __name__ == "__main__":
    main()