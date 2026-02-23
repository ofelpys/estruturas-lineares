class IntSet:
    """Tipo Abstrato de Dados (TAD) que representa um conjunto de inteiros.

    A implementação usa um vetor (lista) de inteiros internamente e garante
    que não haja elementos duplicados. Disponibiliza operações de inserção,
    remoção, consulta do menor e maior valor e tamanho do conjunto.
    """  # definição da classe IntSet

    def __init__(self, elementos=None):
        """Inicializa o conjunto opcionalmente com uma lista de inteiros.

        Elementos repetidos são ignorados na criação.
        """  # construtor da classe, permite valores iniciais
        self._dados = []  # armazena elementos do conjunto
        if elementos is not None:  # se a lista inicial foi fornecida
            for e in elementos:  # itera pelos elementos
                self.insert(e)  # insere usando método da classe

    def insert(self, value: int) -> None:
        """Insere o inteiro no conjunto se ainda não estiver presente."""  # método de inserção
        if value not in self._dados:  # verifica duplicata
            self._dados.append(value)  # adiciona ao final da lista

    def remove(self, value: int) -> None:
        """Remove o inteiro do conjunto. Levanta ValueError se não existir."""  # método de remoção
        try:
            self._dados.remove(value)  # tenta remover o valor
        except ValueError:
            # se valor não estiver, lança exceção com mensagem clara
            raise ValueError(f"Valor {value} não pertence ao conjunto")

    def min_value(self) -> int:
        """Retorna o menor valor do conjunto. Levanta ValueError se vazio."""  # consulta menor elemento
        if not self._dados:  # se lista estiver vazia
            raise ValueError("Conjunto vazio")
        return min(self._dados)  # usa função built-in min

    def max_value(self) -> int:
        """Retorna o maior valor do conjunto. Levanta ValueError se vazio."""  # consulta maior elemento
        if not self._dados:
            raise ValueError("Conjunto vazio")
        return max(self._dados)  # usa função built-in max

    def size(self) -> int:
        """Retorna o número de elementos do conjunto."""  # retorna comprimento do vetor
        return len(self._dados)

    def __repr__(self) -> str:
        # representação de depuração que mostra o conteúdo da lista
        return f"IntSet({self._dados})"
