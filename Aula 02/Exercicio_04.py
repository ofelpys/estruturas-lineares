##AULA 02
##Exercício 04
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026
from classe4 import Saldo

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 04<<<<<<<<<<<<<<<<<<<<<<\n")

    x = float(input("Entre com seu saldo:\n"))

    calc = Saldo(x)

    print("Seu novo saldo é:{:.2f}".format(calc.saldo_novo()))

if __name__ == "__main__":
    main()