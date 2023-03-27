from Conta import Conta

#Classe Conta_corrente(filha)
#Utiliza o Princípio O.L.I.D. da SOLID

class Conta_corrente(Conta):
    def __init__(self, saldo):
        super().__init__(ID_conta= None, saldo=saldo)
        print("Você selecionou: Conta Corrente\n")
        
    def saque(self, valorSaque):
        if(valorSaque <= self.saldo):
            self.saldo = self.saldo - valorSaque
            print(f"Você sacou: {valorSaque:.2f} e ficou com {self.saldo:.2f} em sua conta.")
        else:
            print("Não é possível sacar um valor que você NÃO POSSUI !!!")

    def saqueEspecial(self, valorSaque):
        creditoEspecial = (self.saldo / 2)#credito especial é metade do saldo em conta
        
        if(valorSaque <= (self.saldo + creditoEspecial)):
            self.saldo = (self.saldo + creditoEspecial)

            self.saldo = self.saldo - valorSaque
            print(f"Você sacou: {valorSaque:.2f} utilizando Seu Crédito Especial e ficou com {self.saldo:.2f} de crédito especial em sua conta.")
        else:
            print("Não é possível sacar esse Valor, NEM COM CRÉDITO ESPECIAL!")

    def Deposito(self, valorDeposito):
        self.saldo = self.saldo + valorDeposito
        print(f"Você Depositou {valorDeposito:.2f} seu saldo agora é: {self.saldo:.2f}")
 