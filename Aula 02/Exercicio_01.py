##AULA 02
##Exercício 01
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe1 import Media

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<") 
    print(">>>>>>>>>>>>>>>>>>>>>>Exercício 01<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>>>>>>>Calculo de Média<<<<<<<<<<<<<<<<<<<<<<")

    x = float(input("Digite o Primeiro Número para o cálculo:\n"))
    y = float(input("Digite o segundo número para o cáculo:\n"))

    calc = Media(x,y)

    print(f"A média será: {calc.media()}")

if __name__ == "__main__":
    main()
