# importa a classe Sphere do módulo sphere
from sphere import Sphere


# função principal do programa
def main():
    # comentário: demonstra como usar o TAD Esfera
    try:
        # lê uma string do usuário e tenta converter para float
        r = float(input("Digite o raio da esfera: "))
    except ValueError:
        # se a conversão falhar, avisa e define valor padrão
        print("Raio inválido. Utilizando valor padrão 1.0.")
        r = 1.0

    # cria uma instância de Sphere usando o raio lido
    esfera = Sphere(r)
    # imprime o raio obtido através do método get_radius()
    print(f"Raio: {esfera.get_radius()}")
    # calcula e exibe a área da superfície com 4 casas decimais
    print(f"Área da superfície: {esfera.area():.4f}")
    # calcula e exibe o volume com 4 casas decimais
    print(f"Volume: {esfera.volume():.4f}")


# garante que main() seja executada apenas quando o arquivo for rodado diretamente
if __name__ == "__main__":
    main()
