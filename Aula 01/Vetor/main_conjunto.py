# importa a classe IntSet definida em int_set.py
from int_set import IntSet


# função de demonstração principal

def main():
    """Programa principal de demonstração do TAD IntSet."""  # descrição da função
    conjunto = IntSet()  # inicializa conjunto vazio
    # exibe mensagem sobre os valores que serão inseridos
    print("Inserindo alguns valores no conjunto: 4, 1, 7, 1, 3")
    for v in [4, 1, 7, 1, 3]:  # iterar sobre cada valor
        conjunto.insert(v)  # insere no conjunto (duplica ignorada)
    print(f"Conjunto atual: {conjunto}")  # mostra estado atual
    print(f"Menor valor: {conjunto.min_value()}")  # consulta menor elemento
    print(f"Maior valor: {conjunto.max_value()}")  # consulta maior elemento
    print(f"Tamanho: {conjunto.size()}")  # exibe tamanho do conjunto

    print("\nTentando remover 7 e 2...")  # mensagem de remoção
    try:
        conjunto.remove(7)  # tenta remover valor existente
        print("7 removido com sucesso.")
    except ValueError as e:
        print(e)  # mostra erro se não puder remover
    try:
        conjunto.remove(2)  # tenta remover valor ausente
        print("2 removido com sucesso.")
    except ValueError as e:
        print(e)  # exibe mensagem de erro

    print(f"Conjunto final: {conjunto}")  # mostra conjunto após operações


# bloco de proteção para execução como script
if __name__ == "__main__":
    main()  # chama a função principal
