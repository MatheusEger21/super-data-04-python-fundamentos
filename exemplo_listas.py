def exemplo_lista_simples():
    #CRUD - CREATE - READ - UPDATE - DELETE

    # CRIANDO UMA LISTA COM UM ELEMENTO (NÃO É OBRIGATPRIO COLOCAR ITEM NA LISTA AO CRIAR)

    colegas: list[str] = ["Pedro"]
    # ADICIONANDO ELEMENTOS NA LISTA/VETOR
    colegas.append("Judity")
    colegas.append("Juliana")
    colegas.append("Francisco")

    #REMOVER O FRANCISCO
    colegas.remove("Francisco")

    # ALTERANDO O NOME DA JULIANA NA TERCEIRA POSIÇÃO
    colegas[2] = "Liana"

    # APRESENTANDO A QUANTIDADE DE ELEMENTOS DA LISTA

    print("Quantidade de coleguinhas: ", len(colegas))

    # APRESENTAR OS ELEMENTOS DA LISTA
    print("Primeiro Colega: ", colegas[0])
    print("Segundo Colega: ", colegas[1])
    print("Terceiro Colega: ", colegas[2])


def exemplo_lista_simples_int():
    numeros: list[int] = []

    # SOLICITAR UM NUMERO E ADICIONAR NA LISTA(POSIÇÃO 0)
    numeros.append(int(input("Digite um numero: ")))
    numeros.append(int(input("Digite um numero: ")))
    numeros.append(int(input("Digite um numero: ")))

    soma: int = numeros[0] + numeros[1] + numeros [2]
    print("Soma: ", soma)


def exemplo_lista_simples_percorrendo():
    salarios: list[float] = []

    # quantidade_desejada: int = int(input("Digite a quantidade de salarios: "))

    # SOLICITAR PARA O USUÁRIO 4 SALARIO

    for i in range(0 ,4):
        salario = float(input("Digite o salário: "))

        salarios.append(salario)

    # soma = salario[0] + salario[1] + salario[2] + salario[3]
    soma: float = 0
    for i in range(0, 4):
        soma = soma + salarios[i]

    # QUAL MAIOR SALARIO
    maior_salario: float = 0
    for i in range(0, 4):
        salario_atual = salarios[i]
        if salario_atual > maior_salario:
            maior_salario = salario_atual

    # QUAL O MENOR SALARIO
    menor_salario: float = 999999999
    for i in range(0, 4):
        salario_atual: float = salarios[i]
        if salario_atual < menor_salario:
            menor_salario = salario_atual

    media: float = soma / len(salarios)

    # APRESENTAR SALARIOS
    for i in range(0, 4):
        salario_atual: float = salarios[i]
        print(f"Sálario {(i + 1)}º: R$ {salario_atual}")

    print("Soma: ", soma)
    print("Média: ", media)
    print("Maior Salário: ", maior_salario)
    print("Menor Salário ", menor_salario)

    

if __name__ == "__main__":
    exemplo_lista_simples_percorrendo()