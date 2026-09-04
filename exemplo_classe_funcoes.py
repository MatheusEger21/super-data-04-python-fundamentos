import os

def limpar_terminal():
    os.system("cls")

class ContaBancaria:
    #Construtor
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        #saldo recebe ele mesmo + valor a depoitar
        self.saldo = self.saldo + valor
        print("Depositando R$ ", valor)

    def sacar(self, valor: float):
        #se saldo maio ou igual que o valor
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            #serve para dizer que o saque foi realizado com sucesso
            return True
        else:
            return False

def exemplo_conta_bancaria():
    zeh_conta: ContaBancaria = ContaBancaria("Zeh da Conta", 500.00)
    print("Conta: ", zeh_conta.titular)
    print("Saldo: ", zeh_conta.saldo)

    zeh_conta.depositar(250)
    print("Saldo: ",zeh_conta.saldo)
    if zeh_conta.sacar(300) == True:
        print("Saque realizado com sucesso: R$ 300,00")
    else:
        print("Não foi possível sacar R$ 300,00")

def exemplo_conta_bancaria_com_usuario():
    titular = input("Digite o nome do titular: ")
    saldo_inicial = float(input(" Digite o saldo inicial: "))

    limpar_terminal()
    conta_bancaria: ContaBancaria = ContaBancaria(titular, saldo_inicial)

    menu = """Bem vindo ao sistema do Banco XYZ
    1 - Saldo
    2 - Depositar
    3 - Sacar
    9 - Sair
    Escolha a opção desejada:"""
    opcao = int(input(menu))
    #enquanto opcao for diferente de 9 repetir
    while opcao != 9:
        limpar_terminal()

        if opcao == 1:
            print("Conta: ", conta_bancaria.titular)
            print("Saldo: ", conta_bancaria.saldo)
        elif opcao == 2:
            valor_depositar = float(input("Digite o valor para depositar: "))
            conta_bancaria.depositar(valor_depositar)
        elif opcao == 3:
            valor_sacar = float(input("Digite o valor para sacar: "))
            resultado_saque = conta_bancaria.sacar(valor_sacar)
            if resultado_saque == True:
                print("Saque realizado com sucesso")
            else:
                print("Saque não realizado por saldo insuficiente")

        opcao = int(input(menu))
    limpar_terminal()
    print("Obrigado por utilizar o Banco XYZ")

if __name__ == "__main__":
    exemplo_conta_bancaria_com_usuario()