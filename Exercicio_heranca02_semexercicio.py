class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor: int):
        self.velocidade = self.velocidade + valor

    def frear(self, valor):
        self.velocidade = self.velocidade - valor

        if self.velocidade < 0:
            self.velocidade = 0

class Carro(Veiculo):

    def __init__(self, marca, modelo, quantidade_portas):

        # Inicializa as propriedades da classe pai
        super().__init__(marca, modelo)

        # Propriedade específica do Carro
        self.quantidade_portas = quantidade_portas

    def apresentar_dados(self):

        if self.velocidade == 0:
            print("A velocidade do carro não pode ser 0.")
        else:
            print("----- DADOS DO CARRO -----")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Velocidade atual: {self.velocidade} km/h")
            print(f"Quantidade de portas: {self.quantidade_portas}")

class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):

        # Inicializa as propriedades da classe pai
        super().__init__(marca, modelo)

        # Propriedade específica da Moto
        self.cilindradas = cilindradas

    def apresentar_dados(self):
        if self.velocidade == 0:
            print("A velocidade da moto não pode ser 0.")    
        else:
            print("----- DADOS DA MOTO -----")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Velocidade atual: {self.velocidade} km/h")
            print(f"Cilindradas: {self.cilindradas} cc")


def exemplo_veiculos():

    carro = Carro("Volkswagen", "Golf", 4)

    # Acelera o carro
    carro.acelerar(80)

    # Freia o carro
    carro.frear(30)

    # Apresenta os dados
    carro.apresentar_dados()

    print()

    moto = Moto("Honda","CB 500",500)

    # Acelera a moto
    moto.acelerar(100)

    # Freia a moto
    moto.frear(40)

    # Apresenta os dados
    moto.apresentar_dados()


if __name__ == "__main__":
    exemplo_veiculos()