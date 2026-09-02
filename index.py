class colaborador:
    #Contrutor
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias
        # Calculando e armazenando dentro de um atributo do objeto
        self.ano_nascimento = 2026 - self.idade


#Função sem parametros
def exemplo_colaborador():
    #Instanciar(Criar) um objeto da classe Colaborador
    #       Colaborador(nome, idade, peso, tem_ferias)
    antonio = colaborador("Antonio", 38, 108, True)

    #calculando o ano de nascimento do Antonio
    #antonio_ano_nascimento = 2026 - antonio.idade

    marcus = colaborador("Marcus", 40, 80, False)

    #marcus_ano_nascimento = 2026 - marcus.idade

    print("Colaborador 1:", antonio.nome)
    print("Idade:", antonio.idade)
    print("Ano de Nascimento:", antonio.ano_nascimento)
    print("Peso:", antonio.peso)
    print("Tem Férias?", antonio.tem_ferias, end="\n\n\n")
          
    print("Colaborador 2:", marcus.nome)
    print("Idade:", marcus.idade)
    print("Ano de Nascimento:", marcus.ano_nascimento)
    print("Peso:", marcus.peso)
    print("Tem Férias?", marcus.tem_ferias)


class aluno:
    # Método construtor
    def __init__(self, nome: str, nota1: float, nota2: float, nota3: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        # self.media = self.nota1 + self.nota2 + self.nota3) / 3

    # função que retorna um float
    def calcular_media(self) -> float:
        media: float = (self.nota1 + self.nota2 + self.nota3) / 3
        return round(media, 2)

def exemplo_aluno():
    # Instanciando um objeto(Matheus) da classe aluno
    matheus: aluno = aluno("Matheus da Silva", 7, 4.5, 10)

    lukas: aluno = aluno("Lukas Pettry", 9.5, 9.8, 0)

    #matheus_media = round((matheus.nota1 + matheus.nota2 + matheus.nota3) / 3, 2)
    matheus_media = matheus.calcular_media()
    #lukas_media = round((lukas.nota1 + lukas.nota2 + lukas.nota3) / 3, 2)
    lukas_media = lukas.calcular_media()

    matheus_status = ""
    if matheus_media < 7:
        matheus_status = "Reprovado"
    else:
        matheus_status = "Aprovado"

    lukas_status = ""
    if lukas_media < 7:
        lukas_status = "Reprovado"
    else:
        lukas_status = "Aprovado"

    print(" Aluno: ", matheus.nome)
    print(" Nota 1: ", matheus.nota1)
    print(" Nota 2: ", matheus.nota2)
    print(" Nota 3: ", matheus.nota3)
    print(" Média : ", matheus_media)
    print(" Status: ", matheus_status)

    print("\n Aluno: ", lukas.nome)
    print(" Nota 1: ", lukas.nota1)
    print(" Nota 2: ", lukas.nota2)
    print(" Nota 3: ", lukas.nota3)
    print(" Média : ", lukas_media)
    print(" Status: ", lukas_status)

class Brinquedo:
    # Método construtor
    def __init__(self, marca: str, nome: str, classificacao: int, preco: float):
        self.marca = marca
        self.nome = nome
        self.classificacao = classificacao
        self.preco = preco

def exemplo_brinquedo():
    # Instanciando um objeto(MAtheus) da classe aluno
    hotwhells: Brinquedo = Brinquedo("Hotwhells", "Porshe", 4, 154.34)

    boneca: Brinquedo = Brinquedo("Barbie", "Barbie Quero Ser Salva Vidas", 3, 224.49)

    preco_total_brinquedo: float = hotwhells.preco + boneca.preco


    print(" === Brinquedo 1 ===")
    print(f" Marca: {hotwhells.marca}")
    print(f" Nome: {hotwhells.nome}")
    print(f" Classificação : {hotwhells.classificacao}")
    print(f" Preço: R$ : {hotwhells.preco:.2f}")

    print("\n === Brinquedo 2 ===")
    print(f" Marca: {boneca.marca}")
    print(f" Nome: {boneca.nome}")
    print(f" Classificação : {boneca.classificacao}")
    print(f" Preço: R$ : {boneca.preco:.2f}")

    print(f"\nPreço total dos brinquedos: R$ {preco_total_brinquedo:.2f}")

class Flor:
    # Método construtor
    def __init__(self, nome: str, cor: str,):
        self.nome = nome
        self.cor = cor


def exemplo_flor():
    # Instanciando um objeto(MAtheus) da classe aluno
    flor1: Flor = Flor("Rosa", "Vermelha")

    flor2: Flor = Flor("Orquidea", "Amarela")


    print(" === Flor 1 ===")
    print(f" Nome: {flor1.nome}")
    print(f" Cor: {flor1.cor}")

    print("\n === Flor 2 ===")
    print(f" Nome: {flor2.nome}")
    print(f" Cor: {flor2.cor}")

class Livro:
    # Método construtor
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas


def exemplo_livro():
    # Instanciando um objeto(MAtheus) da classe aluno
    livro1: Livro = Livro("Harry Potter e o Enigma do Príncipe", "J. K. Rowling", 2005, 432)

    livro2: Livro = Livro("A Tormenta de Espadas", "George R. R. Martin", 2000, 832)

    total_paginas = livro1.numero_paginas + livro2.numero_paginas


    print(" === Livro 1 ===")
    print(f" Título: {livro1.titulo}")
    print(f" Autor: {livro1.autor}")
    print(f" Ano Publicação: {livro1.ano_publicacao}")
    print(f" Número de páginas: {livro1.numero_paginas}")


    print(" \n=== Livro 2 ===")
    print(f" Título: {livro2.titulo}")
    print(f" Autor: {livro2.autor}")
    print(f" Ano Publicação: {livro2.ano_publicacao}")
    print(f" Número de páginas: {livro2.numero_paginas}")

    print(f" Total de Páginas: {total_paginas}")
    
class PesquePague:
    # Método construtor
    def __init__(self, nome: str, peso: int, preco_kg: float):
        self.nome = nome
        self.peso = peso
        self.preco_kg = preco_kg

    def calcular_total_peixe(self) -> float:
        total_pago: float = self.peso * self.preco_kg
        return total_pago


def exemplo_pesquepague():
    # Instanciando um objeto(MAtheus) da classe aluno
    peixe1: PesquePague = PesquePague("Tilapia", 2.3, 42.80)
    peixe2: PesquePague = PesquePague("Tainha", 4.1, 37.80)
    peixe3: PesquePague = PesquePague("Pacu", 7.2, 51.20)

    total_peixe1 = peixe1.calcular_total_peixe()
    total_peixe2 = peixe2.calcular_total_peixe()
    total_peixe3 = peixe3.calcular_total_peixe()

    total_pedido = total_peixe1 + total_peixe2 + total_peixe3


    print(" \n=== Peixe 1 ===")
    print(f" Nome: {peixe1.nome}")
    print(f" Peso: {peixe1.peso}")
    print(f" Preço por KG: {peixe1.preco_kg}")
    print(f" Valor do peixe: R$  {total_peixe1:.2f}")


    print(" \n=== Peixe 2 ===")
    print(f" Nome: {peixe2.nome}")
    print(f" Peso: {peixe2.peso}")
    print(f" Preço por KG: {peixe2.preco_kg}")
    print(f" Valor do peixe: R$  {total_peixe2:.2f}")

    print(" \n=== Peixe 3 ===")
    print(f" Nome: {peixe3.nome}")
    print(f" Peso: {peixe3.peso}")
    print(f" Preço por KG: {peixe3.preco_kg}")
    print(f" Valor do peixe: R$  {total_peixe3:.2f}")

    print(f"\n Total do pedido: {total_pedido:.2f}")

class Calculadora:
    # Método construtor
    def __init__(self, numero1: float, numero2: float):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        return self.numero1 / self.numero2


def exemplo_calculadora():
    # Instanciando um objeto(MAtheus) da classe aluno
    calculadora = Calculadora(10, 5)

    # Chamando as funções e apresentando os resultados
    print(f"Soma: {calculadora.somar()}")
    print(f"Subtração: {calculadora.subtrair()}")
    print(f"Multiplicação: {calculadora.multiplicar()}")
    print(f"Divisão: {calculadora.dividir()}")


# Ponto de inicio da aplicação
if __name__ == "__main__":
    # Executar a função do colaborador
    exemplo_calculadora()

# Executar = py index.py
#git status
#git add .
#git commit -m "Exemplos de Classes"
#git push origin main