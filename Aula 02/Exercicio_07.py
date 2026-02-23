##AULA 02
##Exercício 07
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe7 import Bhaskara

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 06<<<<<<<<<<<<<<<<<<<<<<\n")

    print("Cálculo de Bhaskara:")
    a = float(input("Digite o valor de A:\n"))
    b = float(input("Digite o valor de B:\n"))
    c = float(input("Digite o valor de C:\n"))

    calc = Bhaskara(a,b,c)

    print(calc.raizes())

if __name__ == "__main__":
    main()