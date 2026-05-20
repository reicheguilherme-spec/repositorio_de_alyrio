saldo = 1000
print("Seja bem vindo ao nosso sistema!")
print("Escolha uma das opções abaixo: ")
print("Opção 1 - Consultar saldo\nOpção 2 - Realizar depósito\nOpção 3 - Realizar Saque\nOpçao 4 - Sair")
opcao = int(input("Qual a opção escolhida?: "))
if opcao <1 or opcao>4:
    print("Opçao inválida!")

if opcao == 1:
    print(saldo)
elif opcao == 2:
    deposito = float(input("Quanto deseja depositar?: "))
    saldo = saldo + deposito
    print(f"Depósito realizado com sucesso, seu novo saldo é de: {saldo:.2f}")
elif opcao == 3:
    saque = float(input("Quanto deseja sacar?: "))
    saldo = saldo - saque
    print("Saque realizado com sucesso! Seu novo saldo é de: ", saldo)

elif opcao == 4:
    print("Obrigado por usar nosso programa!")