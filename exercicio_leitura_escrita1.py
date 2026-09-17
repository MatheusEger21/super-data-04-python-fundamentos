
def escrever_arquivo_numeros():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("9\n")
        arquivo.write("5\n")
        arquivo.write("12\n")
        arquivo.write("21\n")
        arquivo.write("20\n")
        arquivo.write("90\n")
        
        print("Arquivo 'numeros.txt' criado com sucesso")



def ler_arquivo_numeros():
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazenando na variavel conteudo (STR)
        conteudo = arquivo.read()
        print("Conteudo do arquivo 'numeros.txt':")
        print(conteudo)


if __name__ == "__main__":
    ler_arquivo_numeros()