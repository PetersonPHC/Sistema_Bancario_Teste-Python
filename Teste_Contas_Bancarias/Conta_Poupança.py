from Conta import Conta

#Classe Conta_poupanca(filha)
#Utiliza os Princípios O.L.I. da SOLID
class Conta_poupanca(Conta):
    def __init__(self, saldo):
        super().__init__(ID_conta= None, saldo= saldo)
        print("Você Selecionou: Conta Poupança\n")

    def saque(self, valorSaque):
        if(valorSaque <= self.saldo):
            self.saldo = self.saldo - valorSaque
            print(f"Você sacou: {valorSaque:.2f} e ficou com {self.saldo:.2f} em sua conta.")
        else:
            print("Não é possível sacar um valor que você NÃO POSSUI !!!")

    def Deposito(self, valorDeposito):
        self.saldo = self.saldo + valorDeposito
        print(f"Você Depositou {valorDeposito:.2f} seu saldo agora é: {self.saldo:.2f}")

    def saberRendimento(self):
        print("Temos o Melhor Redimento do Mundo!")
        print("Digite 1 Para: Rendimento por Segundo - (Percentual de rendimento 0,00002314%)")
        print("Digite 2 Para: Rendimento por Minuto - (Percentual de rendimento 0,001388%)")
        print("Digite 3 Para: Rendimento por Hora - (Percentual de rendimento 0,083%)")
        print("Digite 4 Para: Rendimento por Dia - (Percentual de rendimento 2%)")
        print("Digite 5 Para: Rendimento por Mês - (Percentual de rendimento 60%)")
        print("Digite 6 Para: Rendimento por Ano - (Percentual de rendimento 720%)")
        periodo = int(input("Insira o valor numérico para o tipo de período desejado: "))
        match periodo:
            case 1:#Segundos
                rendimento = (self.saldo * (0.00002314/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.3f} por Segundo")
            case 2:#Minutos
                rendimento = (self.saldo * (0.001388/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.3f} por Minuto")
            case 3:#Horas
                rendimento = (self.saldo * (0.083/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.2f} por Hora")
            case 4:#Dias
                rendimento = (self.saldo * (2/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.2f} por Dia")
            case 5:#Meses
                rendimento = (self.saldo * (60/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.2f} por Mês")
            case 6:#Anos
                rendimento = (self.saldo * (720/100))
                return print(f"Seu Saldo é de:{self.saldo:.2f} e Seu Dinheiro está rendendo R${rendimento:.2f} por Ano")
