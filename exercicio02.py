
# ============================================================
# EXERCÍCIO 2 - CINEMA
# ============================================================


class SessaoCinema:

    def __init__(self, filme, tipo_sala, quantidade_ingressos, valor_ingresso):
        self.filme = filme
        self.tipo_sala = tipo_sala
        self.quantidade_ingressos = quantidade_ingressos
        self.valor_ingresso = valor_ingresso

    # --------------------------------------------------------
    # MÉTODO: calcular_total()
    # --------------------------------------------------------

    def calcular_total(self):
        return self.quantidade_ingressos * self.valor_ingresso

    # --------------------------------------------------------
    # MÉTODO: calcular_desconto()
    # --------------------------------------------------------

    def calcular_desconto(self):

        total = self.calcular_total()

        if self.quantidade_ingressos < 5:
            return 0

        elif self.quantidade_ingressos <= 9:
            return total * 0.05

        else:
            return total * 0.10

    # --------------------------------------------------------
    # MÉTODO: calcular_total_final()
    # --------------------------------------------------------

    def calcular_total_final(self):

        total = self.calcular_total()
        desconto = self.calcular_desconto()

        return total - desconto


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

filme = input("Digite o nome do filme: ")

print("\nTipos de sala:")
print("Normal - R$ 25,00")
print("VIP    - R$ 45,00")
print("IMAX   - R$ 55,00")

tipo_sala = input("\nDigite o tipo da sala: ").strip().lower()

# ------------------------------------------------------------
# VALIDAÇÃO DO TIPO DA SALA
# ------------------------------------------------------------

while tipo_sala not in ["normal", "vip", "imax"]:

    print("\nTipo de sala inválido!")

    tipo_sala = input("Digite Normal, VIP ou IMAX: ").strip().lower()


# ------------------------------------------------------------
# DEFINIÇÃO DO VALOR DO INGRESSO
# ------------------------------------------------------------

if tipo_sala == "normal":
    valor_ingresso = 25

elif tipo_sala == "vip":
    valor_ingresso = 45

else:
    valor_ingresso = 55


# ------------------------------------------------------------
# QUANTIDADE DE INGRESSOS
# ------------------------------------------------------------

quantidade_ingressos = int(
    input("Digite a quantidade de ingressos: ")
)


# ------------------------------------------------------------
# CRIAÇÃO DO OBJETO
# ------------------------------------------------------------

sessao = SessaoCinema(
    filme,
    tipo_sala,
    quantidade_ingressos,
    valor_ingresso
)


# ------------------------------------------------------------
# CÁLCULOS
# ------------------------------------------------------------

total = sessao.calcular_total()
desconto = sessao.calcular_desconto()
total_final = sessao.calcular_total_final()


# ------------------------------------------------------------
# EXIBIÇÃO DOS RESULTADOS
# ------------------------------------------------------------

print("\n==============================")
print("       RESUMO DA SESSÃO")
print("==============================")

print(f"Filme: {sessao.filme}")
print(f"Tipo da sala: {sessao.tipo_sala.upper()}")
print(f"Quantidade de ingressos: {sessao.quantidade_ingressos}")
print(f"Valor do ingresso: R$ {sessao.valor_ingresso:.2f}")
print(f"Valor total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")

print("==============================")
