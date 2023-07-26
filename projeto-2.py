def deposito(saldo, valor_deposito, extrato, /):
    while valor_deposito <= 0:
        valor_deposito = float(input(f"Valor inválido. \nPor favor, digite novamente o valor de depósito:\n"))
    saldo += valor_deposito
    extrato = extrato + f"Depósito de R$ {valor_deposito:.2f}\n"
    print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso.")

    return saldo, extrato


def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):

    if valor_saque <= 0:
        print(f"Valor de saque inválido.")
    elif valor_saque > limite:
        print(f"Desculpa, o valor informado excede o limite.")
    elif valor_saque > saldo:
        print(f"Desculpa, você não tem saldo suficiente.")
    elif numero_saques == limite_saques:
        print(f"Desculpa, você já realizou 3 saques no dia.")
    else:
        saldo -= valor_saque
        extrato = extrato + f"Saque de R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def ver_extrato(saldo, /, *, extrato):

    print("============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================\n")


def criar_usuario(usuarios):
    cpf = input("Insira o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Insira o nome completo: ")
    data_nascimento = input("Insira a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f"\nConta número {numero_conta} criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    print("=============== CONTAS ===============")
    for conta in contas:
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)
    print("======================================\n")


def listar_usuarios(usuarios):
    print("============== USUÁRIOS ==============")
    for usuario in usuarios:
        print(f"""\
            Nome:\t{usuario['nome']}
            Data de Nascimento:\t\t{usuario['data_nascimento']}
            CPF:\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
        """)
    print("======================================\n")


def menu():
    print("=============== MENU ===============")
    escolha = int(input("[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Criar Usuário \n[5] Criar Conta"
                        "\n[6] Listar Usuários \n[7] Listar Contas \n[0] Sair \n"
                        "====================================\n"))
    return escolha


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_existente = 0
    saques_realizados = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:

        escolha = menu()

        if escolha == 1:
            print("=================== ÁREA DEPÓSITO ===================")
            valor = float(input("Digite o valor do depósito: "))
            saldo_existente, extrato = deposito(saldo_existente, valor, extrato)
            print("=====================================================\n")

        elif escolha == 2:
            print("============ ÁREA SAQUE ============")
            valor = float(input("Digite o valor de saque:"))
            saldo_existente, extrato, saques_realizados = saque(saldo=saldo_existente,
                                                                valor_saque=valor,
                                                                extrato=extrato, limite=limite,
                                                                numero_saques=saques_realizados,
                                                                limite_saques=LIMITE_SAQUES)
            print("====================================\n")

        elif escolha == 3:
            ver_extrato(saldo_existente, extrato=extrato)

        elif escolha == 4:
            print("============ ÁREA USUÁRIO ============")
            criar_usuario(usuarios)
        elif escolha == 5:
            print("============ ÁREA CONTAS ============")
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif escolha == 6:
            listar_usuarios(usuarios)
        elif escolha == 7:
            listar_contas(contas)
        elif escolha == 0:
            break
        else:
            print("Erro, informe um número existente no menu")


main()
