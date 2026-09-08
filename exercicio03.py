class VeiculoEstacionado:

    def __init__(self, placa, tipo, quantidade_horas):
        self.placa = placa
        self.tipo = tipo
        self.quantidade_horas = quantidade_horas

        # Define o valor da hora conforme o tipo do veículo
        if self.tipo == "moto":
            self.valor_hora = 4.00

        elif self.tipo == "carro":
            self.valor_hora = 8.00

        elif self.tipo == "caminhonete":
            self.valor_hora = 12.00


    # Calcula o valor total sem desconto
    def calcular_valor(self):
        return self.quantidade_horas * self.valor_hora


    # Calcula o valor do desconto
    def calcular_desconto(self):

        valor_estacionamento = self.calcular_valor()

        # Até 3 horas
        if self.quantidade_horas <= 3:
            desconto = 0

        # De 4 até 7 horas
        elif self.quantidade_horas <= 7:
            desconto = valor_estacionamento * 0.05

        # 8 horas ou mais
        else:
            desconto = valor_estacionamento * 0.10

        return desconto


    # Calcula o valor final
    def calcular_total(self):

        valor_estacionamento = self.calcular_valor()

        desconto = self.calcular_desconto()

        return valor_estacionamento - desconto


    # Adiciona novas horas
    def adicionar_horas(self, horas):

        if horas <= 0:
            print("Não é permitido adicionar zero ou horas negativas.")

        else:
            self.quantidade_horas += horas

            print("Horas adicionadas com sucesso!")

print("=" * 40)
print("SISTEMA DE ESTACIONAMENTO")
print("=" * 40)

# Solicita a placa
placa = input("Digite a placa do veículo: ")


# Solicita e valida o tipo
tipo = input(
    "Digite o tipo do veículo (Moto, Carro ou Caminhonete): "
).lower()


# Validação utilizando while
while tipo not in ["moto", "carro", "caminhonete"]:

    print("Tipo de veículo inválido!")

    tipo = input(
        "Digite novamente (Moto, Carro ou Caminhonete): "
    ).lower()


# Solicita a quantidade de horas
quantidade_horas = int(
    input("Digite a quantidade de horas estacionado: ")
)


# Cria o objeto
veiculo = VeiculoEstacionado(
    placa,
    tipo,
    quantidade_horas
)


# Pergunta se deseja adicionar mais horas
resposta = input(
    "Deseja adicionar mais horas? (S/N): "
).lower()


if resposta == "s":

    horas_adicionais = int(
        input("Digite a quantidade de horas adicionais: ")
    )

    veiculo.adicionar_horas(horas_adicionais)


# Calcula os valores
valor_sem_desconto = veiculo.calcular_valor()

desconto = veiculo.calcular_desconto()

valor_final = veiculo.calcular_total()


# Exibe os resultados
print("\n" + "=" * 40)
print("RESUMO DO ESTACIONAMENTO")
print("=" * 40)

print(f"Placa: {veiculo.placa}")

print(f"Tipo: {veiculo.tipo.capitalize()}")

print(f"Quantidade de horas: {veiculo.quantidade_horas}")

print(f"Valor por hora: R$ {veiculo.valor_hora:.2f}")

print(
    f"Valor sem desconto: "
    f"R$ {valor_sem_desconto:.2f}"
)

print(f"Desconto: R$ {desconto:.2f}")

print(f"Valor final: R$ {valor_final:.2f}")