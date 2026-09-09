# ============================================================
# EXERCÍCIO 1 - HERANÇA COM ANIMAIS
# ============================================================
#
# Crie uma classe chamada Animal.
#
# ------------------------------------------------------------
# CLASSE PAI: Animal
# ------------------------------------------------------------
#
# Propriedades:
#
# nome
# idade
class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
# Crie um método chamado apresentar().
#
# Esse método deve exibir:
#
# Nome do animal
# Idade do animal
#
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
    
#
# ============================================================
# CLASSE FILHA: Cachorro
# ============================================================
#
# Crie uma classe chamada Cachorro que herda de Animal.
#
# Utilize super().__init__() para inicializar:
#
# nome
# idade
#
# Adicione uma nova propriedade:
#
# raca
#
# Crie um método chamado latir().
#
# O método deve exibir:
#
# "Au Au!"
class Cachorro(Animal):

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print("Au Au!", end="\n\n")
#
# ============================================================
# CLASSE FILHA: Gato
# ============================================================
#
# Crie uma classe chamada Gato que herda de Animal.
#
# Utilize super().__init__() para inicializar:
#
# nome
# idade
#
# Adicione uma nova propriedade:
#
# cor
#
# Crie um método chamado miar().
#
# O método deve exibir:
#
# "Miau!"
class Gato(Animal):

    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def miar(self):
        print("Miau!")
#
#
# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
#
# 1. Crie um objeto da classe Cachorro.
#
# Exemplo:
#
# nome  -> Bob
# idade -> 3
# raça  -> Labrador
#
# 2. Utilize o método apresentar().
#
# 3. Utilize o método latir().
cachorro = Cachorro("Bob", 3, "Labrador")

cachorro.apresentar()
print(f"Raça: {cachorro.raca}")
cachorro.latir()

#
#
# 4. Crie um objeto da classe Gato.
#
# Exemplo:
#
# nome  -> Mingau
# idade -> 2
# cor   -> Branco
#
# 5. Utilize o método apresentar().
#
# 6. Utilize o método miar().
gato = Gato("Mingau", 2, "Branco")

gato.apresentar()
print(f"Cor: {gato.cor}")
gato.miar()
#
# ============================================================
# OBJETIVO
# ============================================================
#
# Praticar:
#
# - Classe pai
# - Classe filha
# - Herança
# - super().__init__()
# - Métodos herdados