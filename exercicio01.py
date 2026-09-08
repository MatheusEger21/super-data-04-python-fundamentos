class Vendedor:

    def __init__(self, nome, cargo, quantidade_vendas):
        self.nome = nome
        self.cargo = cargo
        self.quantidade_vendas = quantidade_vendas

        # Define o valor da comissão conforme o cargo
        if cargo == "Junior":
            self.valor_comissao = 20
        elif cargo == "Pleno":
            self.valor_comissao = 35
        elif cargo == "Senior":
            self.valor_comissao = 50

    def calcular_comissao(self):
        return self.quantidade_vendas * self.valor_comissao

    def calcular_bonus(self):

        comissao = self.calcular_comissao()

        if self.cargo == "Junior":
            bonus = comissao * 0.10

        elif self.cargo == "Pleno":
            bonus = comissao * 0.20

        elif self.cargo == "Senior":
            bonus = comissao * 0.30

        return bonus

    def calcular_total_receber(self):

        comissao = self.calcular_comissao()
        bonus = self.calcular_bonus()

        return comissao + bonus


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Solicita o nome
while True:

    nome = input("Digite o nome do vendedor: ").strip()

    if 3 <= len(nome) <= 50:
        break

    print("Nome inválido! Digite entre 3 e 50 caracteres.")


# Solicita o cargo
while True:

    cargo = input("Digite o cargo (Junior, Pleno ou Senior): ").strip().capitalize()

    if cargo in ["Junior", "Pleno", "Senior"]:
        break

    print("Cargo inválido! Escolha Junior, Pleno ou Senior.")


# Solicita a quantidade de vendas
while True:

    try:
        quantidade_vendas = int(
            input("Digite a quantidade de vendas realizadas: ")
        )

        if quantidade_vendas >= 0:
            break

        print("A quantidade de vendas não pode ser negativa.")

    except ValueError:
        print("Digite um número inteiro válido.")


# Cria o objeto
vendedor = Vendedor(
    nome,
    cargo,
    quantidade_vendas
)


# Calcula os valores
comissao = vendedor.calcular_comissao()
bonus = vendedor.calcular_bonus()
total = vendedor.calcular_total_receber()


# ============================================================
# RESULTADO
# ============================================================

print("\n" + "=" * 40)
print("        DADOS DO VENDEDOR")
print("=" * 40)

print(f"Nome: {vendedor.nome}")
print(f"Cargo: {vendedor.cargo}")
print(f"Quantidade de vendas: {vendedor.quantidade_vendas}")
print(f"Valor da comissão: R$ {comissao:.2f}")
print(f"Valor do bônus: R$ {bonus:.2f}")
print(f"Total a receber: R$ {total:.2f}")

print("=" * 40)