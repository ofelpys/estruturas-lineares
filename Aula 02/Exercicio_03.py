##AULA 02
##Exercício 03
##PROFESSOR ADILSON LIMA
##DATA: 22/02/2026

from classe3 import Combustivel

def main():
    print(">>>>>>>>>>>>>>>>>>>>>>Seja Bem Vindo<<<<<<<<<<<<<<<<<<<<<<\n") 
    print(">>>>>>>>>>>>>>>>>>>>>>>Exercício 03<<<<<<<<<<<<<<<<<<<<<<\n")

    x = float(input("Entre com a distancia percorrida:\n"))
    y = float(input("Entre com o Combustivel Consumido:\n"))

    calc = Combustivel(x,y)

    print(f"O Conseumo será: {calc.consumo()} Km/L")

if __name__ == "__main__":
    main()