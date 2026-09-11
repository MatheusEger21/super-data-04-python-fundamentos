def exemplo_dicionario_simples():
    # DICIONARIO É UM LUGAR ONDE É POSSIVEL ARMAZENAR VALOR UTILIZANDO UMA CHAVE
    # dict[chave, valor]

    carros: dict[str, str] = {}

    # ARMAZENAR UM DADO DO DICIONARIO PASSANDO O NOME DA CHAVE "VW"
    carros["vw"] = "Fusca"
    carros["gm"] = "Opala"
    carros["byd"] = "Song Plus"

    # ACESSAR O VALOR ARMAZENADO NA CHAVE 'VW"
    print("Valores armazenados nos dicionarios:")
    print(carros["vw"])
    print(carros["gm"])
    print(carros["byd"])

    print("\n")
    print("Chaves:", carros.keys())
    print("Valores:", carros.values())

def exemplo_dicionario_completo():
    alunos: dict[str, dict[str, str | int]] = {}

    alunos["89201"] = {
        "nome": "Pedro",
        "idade": 23,
        "CPF": "201.312.231-30",
    }

    alunos["89202"] = {
        "nome": "Judity da Silva",
        "idade": 39,
        "CPF": "293.120.492-31"
    }
    print("Nome da Judity: ", alunos["89202"]["nome"])
    print("Idade da Judity: ", alunos["89202"]["idade"])
    print("CPF da Judity: ", alunos["89202"]["CPF"])


if __name__ == "__main__":
    exemplo_dicionario_completo()    


