class colaborador:
    #Contrutor
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias


#Função sem parametros
def exemplo_colaborador():
    #Instanciar(Criar) um objeto da classe Colaborador
    #       Colaborador(nome, idade, peso, tem_ferias)
    antonio = colaborador("Antonio", 38, 108, True)

    #calculando o ano de nascimento do Antonio
    antonio_ano_nascimento = 2026 - antonio.idade

    marcus = colaborador("Marcus", 40, 80, False)

    marcus_ano_nascimento = 2026 - marcus.idade

    print("Colaborador 1:", antonio.nome)
    print("Idade:", antonio.idade)
    print("Ano de NAscimento:", antonio_ano_nascimento)
    print("Peso:", antonio.peso)
    print("Tem Férias?", antonio.tem_ferias, end="\n\n\n")
          
    print("Colaborador 1:", marcus.nome)
    print("Idade:", marcus.idade)
    print("Ano de NAscimento:", marcus_ano_nascimento)
    print("Peso:", marcus.peso)
    print("Tem Férias?", marcus.tem_ferias)


class aluno:
    # Método construtor
    def __init__(self, nome: str):
        self.nome = nome

def exemplo_aluno():
    # Instanciando um objeto(MAtheus) da classe aluno
    matheus: aluno = aluno("Matheus da Silva")

    print("Aluno: ", matheus.nome)


# Ponto de inicio da aplicação
if __name__ == "__main__":
    # Executar a função do colaborador
    exemplo_aluno()
    
# Executar = py index.py
#git status
#git add .
#git commit -m "Exemplos de Classes"
#git push origin main