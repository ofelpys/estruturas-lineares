import math  # módulo de funções matemáticas

class Sphere:
    """Tipo Abstrato de Dados (TAD) representando uma esfera.

    A esfera é definida pelo seu raio. Esta classe fornece
    métodos para obter o raio, a área de superfície e o volume.
    """  # início da definição da classe

    def __init__(self, radius: float):
        """Inicializa a esfera com um raio fornecido.

        Args:
            radius (float): O raio da esfera. Deve ser não-negativo.
        """  # construtor da classe
        if radius < 0:  # validação: não aceitar valores negativos
            raise ValueError("Raio não pode ser negativo")
        self._radius = radius  # armazena o raio na instância

    def get_radius(self) -> float:
        """Retorna o raio da esfera."""  # método acessor simples
        return self._radius

    def area(self) -> float:
        """Calcula e retorna a área de superfície da esfera.

        Fórmula: 4 * pi * r^2
        """  # superfície = 4πr²
        return 4.0 * math.pi * (self._radius ** 2)

    def volume(self) -> float:
        """Calcula e retorna o volume da esfera.

        Fórmula: (4/3) * pi * r^3
        """  # volume = (4/3)πr³
        return (4.0 / 3.0) * math.pi * (self._radius ** 3)
