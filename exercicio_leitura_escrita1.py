# Ex 1
def escrever_arquivo_numeros():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("9\n")
        arquivo.write("5\n")
        arquivo.write("12\n")
        arquivo.write("21\n")
        arquivo.write("20\n")
        arquivo.write("90\n")
        
        print("Arquivo 'numeros.txt' criado com sucesso")


# Ex 2
def ler_arquivo_numeros():
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variavel conteudo (STR)
        conteudo = arquivo.read()
        print("Conteudo do arquivo 'numeros.txt':")
        print(conteudo)


def somar_numeros():

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variável conteudo (STR)
        conteudo = arquivo.read()
        # Separar os números que estão em cada linha
        numeros = conteudo.splitlines()
        soma = 0
        for numero in numeros:
            soma = soma + int(numero)
        print("Soma dos números:", soma)



def calcular_media():

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variável conteudo (STR)
        conteudo = arquivo.read()
        # Separar os números armazenados em cada linha
        numeros = conteudo.splitlines()
        soma = 0
        for numero in numeros:
            soma = soma + int(numero)
        media = soma / len(numeros)
        print(f"Média dos números: {media:.2f}")



def descobrir_menor_numero():
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variável conteudo (STR)
        conteudo = arquivo.read()
        # Separar os números armazenados em cada linha
        numeros = conteudo.splitlines()
        menor = int(numeros[0])
        for numero in numeros:
            numero = int(numero)
            if numero < menor:
                menor = numero
        print("Menor número:", menor)



def descobrir_maior_numero():
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variável conteudo (STR)
        conteudo = arquivo.read()
        # Separar os números armazenados em cada linha
        numeros = conteudo.splitlines()
        maior = int(numeros[0])
        for numero in numeros:
            numero = int(numero)
            if numero > maior:
                maior = numero
        print("Maior número:", maior)


if __name__ == "__main__":
    descobrir_maior_numero()