def lista_produtos():
    #CRUD - CREATE - READ - UPDATE - DELETE

    # CRIANDO UMA LISTA COM UM ELEMENTO (NÃO É OBRIGATPRIO COLOCAR ITEM NA LISTA AO CRIAR)

    produtos: list[str] = ["Sabão"]
    # ADICIONANDO ELEMENTOS NA LISTA/VETOR
    produtos.append("Detergente")
    produtos.append("Esmalte")
    produtos.append("Pneu")
    produtos.append("Borracha")

    #REMOVER O FRANCISCO
    produtos.remove("Detergente")

    # ALTERANDO O NOME DA JULIANA NA TERCEIRA POSIÇÃO
    produtos[3] = "Cachorro"

    produtos.append("Cachaça")
    produtos.append("Refrigerante")

    # APRESENTANDO A QUANTIDADE DE ELEMENTOS DA LISTA

    print("Quantidade de produtos: ", len(produtos))

    # APRESENTAR OS ELEMENTOS DA LISTA
    print("Primeiro Item: ", produtos[0])
    print("Segundo Item: ", produtos[1])
    print("Terceiro Item: ", produtos[2])
    print("Quarto Item: ", produtos[3])
    print("Quinto Item: ", produtos[4])
    print("Sexto Item: ", produtos[5])


def lista_jogos():
    jogos: list[str] = []
    preco_jogos: list[float] = []

    for i in range(0, 5):
        jogo = str(input("Digite o nome do jogo: "))
        jogos.append(jogo)
        preco = float(input("Digite o valor do jogo: "))
        preco_jogos.append(preco)

    for i in range(0, 5):
        print(f"Nome do jogo: {jogos[i]}, esse jogo custa R$ {preco_jogos[i]:.2f}")


    soma: float = 0
    for i in range(0, 5):
        soma = soma + preco_jogos[i]

    print(f"\nValor total dos jogos R$ {soma:.2f}")


if __name__ == "__main__":
    lista_jogos()