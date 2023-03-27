from Conta import Conta
from Conta_Corrente import Conta_corrente
from Conta_Poupança import Conta_poupanca
    
#Arquivo Principal (Testando as classes)
print("*"*40)
print(f"Bem Vindo(a) ao Bando Mainsait\nDigite 1 para - Conta Corrente\n{' '*12} ou\nDigite 2 para - Conta Poupança")
print("*"*40)
cliente = int(input("Insira o tipo de conta: "))#Validação/Tipo de conta
if (cliente == 1):#utilizando os Métodos da Classe Conta_Corrente
    ID = int(input("Insira o ID de sua conta: "))
    saldo = float(input("Insira seu saldo: "))
    conta_cliente = Conta(ID_conta= ID , saldo= saldo)
    conta_cliente = Conta_corrente( saldo= saldo)

    valor_de_saque = float(input("Insira o Valor do Saque: "))
    conta_cliente.saque(valorSaque= valor_de_saque)

    depositando = float(input("Insira o Valor do Depósito: "))
    conta_cliente.Deposito(valorDeposito= depositando)

    valor_de_saque = float(input("Insira o Valor do Saque Especial: "))
    conta_cliente.saqueEspecial(valorSaque= valor_de_saque)

elif(cliente == 2):#utilizando os Métodos da Classe Conta_Poupanca
    ID = int(input("Insira o ID de sua conta: "))
    saldo = float(input("Insira seu saldo: "))
    conta_cliente = Conta(ID_conta= ID , saldo= saldo)
    conta_cliente = Conta_poupanca(saldo= saldo)

    valor_de_saque = float(input("Insira o Valor do Saque: "))
    conta_cliente.saque(valorSaque= valor_de_saque)

    depositando = float(input("Insira o Valor do Depósito: "))
    conta_cliente.Deposito(valorDeposito= depositando)

    print("")#só pra dar +1 espaço
    conta_cliente.saberRendimento()

else:
    print("Este tipo de conta Não Existe")
    SystemExit(0)
