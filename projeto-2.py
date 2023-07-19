"""
                    DESAFIO
Precisamos deixar nosso código mais modularizado, para isso 
vamos criar funções para as operações existentes: sacar,
depositar e visualizar histórico. Além disso, para a versão 2 do
nosso sistema precisamos criar duas novas funções: criar
usuário (cliente do banco) e criar conta corrente (vincular com
usuário).
"""


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


def deposito(saldo, valor_deposito, extrato, /):

    while valor_deposito <= 0:
        valor_deposito = float(input(f"Valor inválido. \nPor favor, digite novamente o valor de depósito:\n"))
    saldo += valor_deposito
    extrato = extrato + f"Depósito de R$ {valor_deposito:.2f}\n"
    print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso.")

    return saldo, extrato


def ver_extrato(saldo, /, *, extrato):
    print("============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================\n")


"""
            NOVAS FUNÇÕES
Precisamos criar duas novas funções: criar usuário e criar conta
corrente. Fique a vontade para adicionar mais funções,
exemplo: listar contas. 
"""

"""
            CRIAR USUÁRIO (CLIENTE)
O programa deve armazenar os usuários em uma lista, um
usuário é composto por: nome, data de nascimento, cpf e
endereço. O endereço é uma string com o formato: logradouro,
nro - bairro - cidade/sigla estado. Deve ser armazenado
somente os números do CPF. Não podemos cadastrar 2
usuários com o mesmo CPF.
"""
def criar_usuario(usuarios):
    pass
"""
            CRAIR CONTA CORRENTE
O programa deve armazenar contas em uma lista, uma conta é
composta por: agência, número da conta e usuário. O numero
da conta é sequencial, iniciando em 1. O número da agência é
fixo: "0001". O usuário pode ter mais de uma conta, mas uma
conta pertence a somente um usuário.
"""
def criar_conta_corrente(AGENCIA, numero_conta, usuarios):
    pass
"""
            DICA
Para vincular um usuário a uma conta, filtre a lista de usuários
buscandp o número do CPF informado para cada usuário da 
lista.
"""


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

        print("===================== MENU =====================")
        escolha = int(input("[1] Depositar \n[2] Sacar \n[3] Extrato \n[0] Sair \n"
                            "================================================\n"))
        if escolha == 1:
            print("================= ÁREA DEPÓSITO =================")
            valor = float(input("Digite o valor de depósito:"))
            saldo_existente, extrato = deposito(saldo_existente, valor, extrato)
            print("===============================================\n")

        elif escolha == 2:

            print("============ ÁREA SAQUE ============")
            valor = float(input("Digite o valor de saque:"))
            saldo_existente, extrato, saques_realizados = saque(saldo=saldo_existente, valor_saque=valor,
                                                                extrato=extrato, limite=limite,
                                                                numero_saques=saques_realizados,
                                                                limite_saques=LIMITE_SAQUES)
            print("====================================\n")

        elif escolha == 3:
            ver_extrato(saldo_existente, extrato=extrato)
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 0:
            break
        else:
            print("Erro, informe um número existente no menu")


main()
