resposta = "SIM"
saldo_novo = 0
saldo = 0
continuar = "SIM"
while resposta != "SIM" or continuar == "SIM":
    print("\nSeja bem vindo ao nosso sistema!")
    print("Escolha uma das opções abaixo: ")
    print("Opção 1 - Consultar saldo\nOpção 2 - Realizar depósito\nOpção 3 - Realizar Saque\nOpçao 4 - Sair")
    opcao = int(input("Qual a opção escolhida?: "))
    print()
    if opcao <1 or opcao>4:
        print("Opçao inválida!")

    if opcao == 1:
        if saldo != saldo_novo:
            print("Seu saldo é de: ",saldo_novo)
        elif saldo == saldo:
            print("Seu saldo é de: ",saldo)
    elif opcao == 2:
        deposito = float(input("Quanto deseja depositar?: "))
        saldo_novo = saldo + deposito
        print(f"Depósito realizado com sucesso, seu novo saldo é de: {saldo_novo:.2f}")
    elif opcao == 3:
        saque = float(input("Quanto deseja sacar?: "))
        saldo_novo = saldo_novo - saque
        print("Saque realizado com sucesso! Seu novo saldo é de: ", saldo_novo)

    elif opcao == 4:
        resposta = input(("Deseja mesmo sair?: ")).upper()
        if resposta == "SIM":
            print("Obrigado por usar nosso sistema, Deus abençoe!")
            break

    continuar = str(input("Deseja continuar?: ")).upper()
    if continuar != "SIM":
        print("Obrigado por usar nosso sistema, Deus abençoe!")
        break

