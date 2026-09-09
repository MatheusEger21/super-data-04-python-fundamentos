# ============================================================
# EXERCÍCIO 2 - SISTEMA DE VEÍCULOS
# ============================================================
#
# Desenvolva um pequeno sistema utilizando HERANÇA.
#
# O sistema deverá possuir uma classe pai chamada Veiculo
# e duas classes filhas:
#
# - Carro
# - Moto
#
# ============================================================
# CLASSE PAI: Veiculo
# ============================================================
#
# Crie uma classe chamada Veiculo.
#
# ------------------------------------------------------------
# PROPRIEDADES
# ------------------------------------------------------------
# marca
# modelo
# velocidade
#
# A velocidade inicial deve começar sempre em 0.
class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0
# ------------------------------------------------------------
# MÉTODO: acelerar(valor)
# ------------------------------------------------------------
#
# Deve aumentar a velocidade atual do veículo.
#
# Exemplo:
#
# velocidade atual = 50
# acelerar(20)
#
# nova velocidade = 70
    def acelerar(self, valor: int):
        self.velocidade = self.velocidade + valor
# ------------------------------------------------------------
# MÉTODO: frear(valor)
# ------------------------------------------------------------
#
# Deve diminuir a velocidade atual do veículo.
#
# A velocidade nunca poderá ficar menor que 0.
#
# Exemplo:
#
# velocidade atual = 30
# frear(50)
#
# nova velocidade = 0
    def frear(self, valor):
        self.velocidade -= valor

        if self.velocidade < 0:
            self.velocidade = 0
# ============================================================
# CLASSE FILHA: Carro
# ============================================================
#
# Crie uma classe chamada Carro que herda de Veiculo.
#
# Utilize super().__init__() para inicializar as propriedades
# herdadas da classe Veiculo.
#
# ------------------------------------------------------------
# PROPRIEDADE ADICIONAL
# ------------------------------------------------------------
#
# quantidade_portas
#
#
# ------------------------------------------------------------
# MÉTODO: apresentar_dados()
# ------------------------------------------------------------
#
# Deve exibir:
#
# - Marca
# - Modelo
# - Velocidade atual
# - Quantidade de portas
class Carro(Veiculo):

    def __init__(self, marca, modelo, quantidade_portas):

        # Inicializa as propriedades da classe pai
        super().__init__(marca, modelo)

        # Propriedade específica do Carro
        self.quantidade_portas = quantidade_portas

    def apresentar_dados(self):
        print("----- DADOS DO CARRO -----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidade atual: {self.velocidade} km/h")
        print(f"Quantidade de portas: {self.quantidade_portas}")
#
#
# ============================================================
# CLASSE FILHA: Moto
# ============================================================
#
# Crie uma classe chamada Moto que herda de Veiculo.
#
# Utilize super().__init__() para inicializar as propriedades
# herdadas da classe Veiculo.
#
# ------------------------------------------------------------
# PROPRIEDADE ADICIONAL
# ------------------------------------------------------------
#
# cilindradas
class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):

        # Inicializa as propriedades da classe pai
        super().__init__(marca, modelo)

        # Propriedade específica da Moto
        self.cilindradas = cilindradas

    
#
# ------------------------------------------------------------
# MÉTODO: apresentar_dados()
# ------------------------------------------------------------
#
# Deve exibir:
#
# - Marca
# - Modelo
# - Velocidade atual
# - Cilindradas

    def apresentar_dados(self):
            print("----- DADOS DA MOTO -----")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Velocidade atual: {self.velocidade} km/h")
            print(f"Cilindradas: {self.cilindradas} cc")
#
# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
#
# Crie uma função chamada exemplo_veiculos().
#
# Dentro dela:
#
# 1. Crie um objeto da classe Carro.
#
# Exemplo de dados:
#
# marca              -> Volkswagen
# modelo             -> Golf
# quantidade_portas  -> 4
#
#
# 2. Utilize o método acelerar() herdado da classe Veiculo.
#
# 3. Utilize o método frear() herdado da classe Veiculo.
#
# 4. Utilize o método apresentar_dados() da classe Carro.
#
#
# 5. Crie um objeto da classe Moto.
#
# Exemplo de dados:
#
# marca        -> Honda
# modelo       -> CB 500
# cilindradas  -> 500
#
#
# 6. Utilize o método acelerar() herdado da classe Veiculo.
#
# 7. Utilize o método frear() herdado da classe Veiculo.
#
# 8. Utilize o método apresentar_dados() da classe Moto.

def exemplo_veiculos():

    # --------------------------------------------------------
    # CARRO
    # --------------------------------------------------------

    carro = Carro("Volkswagen", "Golf", 4)

    # Acelera o carro
    carro.acelerar(80)

    # Freia o carro
    carro.frear(30)

    # Apresenta os dados
    carro.apresentar_dados()


    print()


    # --------------------------------------------------------
    # MOTO
    # --------------------------------------------------------

    moto = Moto("Honda","CB 500",500)

    # Acelera a moto
    moto.acelerar(100)

    # Freia a moto
    moto.frear(40)

    # Apresenta os dados
    moto.apresentar_dados()


if __name__ == "__main__":
    exemplo_veiculos()

#
#
# ============================================================
# OBJETIVO DO EXERCÍCIO
# ============================================================
#
# Praticar os conceitos de:
#
# - Classe pai
# - Classe filha
# - Herança
# - super().__init__()
# - Propriedades herdadas
# - Métodos herdados
# - Métodos específicos das classes filhas
#
#
# Estrutura esperada:
#
# class Veiculo:
#     ...
#
#
# class Carro(Veiculo):
#     ...
#
#
# class Moto(Veiculo):
#     ...
#
#
# def exemplo_veiculos():
#     ...
#
#
# if __name__ == "__main__":
#     exemplo_veiculos()