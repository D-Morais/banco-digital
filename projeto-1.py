menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("================= ÁREA DEPÓSITO =================")
        valor = float(input("Digite o valor de depósito:"))
        while valor <= 0:
            valor = float(input(f"Valor inválido. \nPor favor, digite novamente o valor de depósito:"))
        saldo += valor
        extrato = extrato + f"Depósito de R$ {valor:.2f}\n"
        print("===============================================")
    elif opcao == 2:

        print("============ ÁREA SAQUE ============")
        valor_saque = float(input("Digite o valor de saque:"))
        if valor_saque <= 0:
            print(f"Valor de saque inválido.")
        elif valor_saque > limite:
            print(f"Desculpa, o valor do saque excede o limite.")
        elif valor_saque > saldo:
            print(f"Desculpa, você não tem saldo suficiente.")
        elif LIMITE_SAQUES == 0:
            print(f"Desculpa, você já realizou 3 saques no dia.")
        else:
            saldo -= valor_saque
            extrato = extrato + f"Saque de R$ {valor_saque:.2f}\n"
            LIMITE_SAQUES -= 1
        print("====================================")

    elif opcao == 3:

        print("============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == 0:

        print("Operação finalizada, volte sempre.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
