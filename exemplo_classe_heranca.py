#from datetime import datetime
import datetime

class ContaBancaria: #classe pai
    #__init__ é o contrutor
    def __init__(self, cliente: str, saldo_inicial: float, numero: str):
        self.cliente = cliente
        self.saldo = saldo_inicial
        #encapsulamento publico
        self.numero = numero
        #encapsulamento privado fora da classe não ter acesso
        self.__quantidade_saques = 0

    def sacar(self, valor: float):
        #Ao realizar o Terceiro saque naquele mês, deve gerar uma cobrança de 1,50

        if self.__quantidade_saques >=3:
            valor = valor + 1.50

        if valor > self.saldo:
            print("Saque não realizado por falta de saldo")
            return

        self.saldo = self.saldo - valor
        print("Realizado saque de R$ ", valor, end="\n\n")
        #incrementar a variavel quantidade de saques
        self.__quantidade_saques = self.__quantidade_saques + 1

    # Herança é a capacidade de herdar propriedades(Caracteristicas) e função/metodos(Comportamentos)
    # ContaCorrente é uma classe "Filha" da classe ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, cliente: str, saldo_inicial: float, numero: str, limite_credito: float):
        super().__init__(cliente, saldo_inicial,numero)
        self.limite_credito = limite_credito

    def apresentar_extrato(self):
        data_hora_atual = datetime.datetime.now() # import datetime
        #data_hora_atual = datetime.now() # From datetime import datetime

        print("Extrato: ", data_hora_atual.strftime("%d/%m/%Y %H:%M"))
        print("Cliente: ", self.cliente)
        print("Número: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Limite de crédito: ", self.limite_credito, end="\n\n")


class ContaSalario(ContaBancaria):
    def __init__(self, cliente: str, saldo_inicial: float, numero: str):
        super().__init__(cliente, saldo_inicial, numero)
    #Gerar_extrato
    #Tranferencia
    #Sacar

def exemplo_contas():
    conta_zeh = ContaCorrente("Zeh", 5000, "1234", 2000)
    conta_zeh.apresentar_extrato()
    conta_zeh.sacar(1000)
    conta_zeh.apresentar_extrato()

    conta_judity = ContaSalario("Judity", 145_945.00, "1235")
    conta_judity.sacar(30_000)
    #ContaSalario não tem a função apresentar_extrato, pois pertence a classe ContaCorrente
    conta_judity.apresentar_extrato()

if __name__ == "__main__":
    exemplo_contas()

