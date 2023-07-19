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
    print("============ ÁREA SAQUE ============")

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

    print("====================================")
    return saldo, extrato


"""
            DEPÓSITO
A função depósito deve receber os argumentos apenas por
posição (posicional only). Sugestão de argumentos: saldo, valor,
extrato. Sugestão de retorno: saldo e extrato.    
"""

"""
            Extrato
A função extrato deve receber os argumentos por posição e
nome (positional only e keyword only). Argumentos
posicionais: saldo, argumentos nomeados: extrato.
"""

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

"""
            CRAIR CONTA CORRENTE
O programa deve armazenar contas em uma lista, uma conta é
composta por: agência, número da conta e usuário. O numero
da conta é sequencial, iniciando em 1. O número da agência é
fixo: "0001". O usuário pode ter mais de uma conta, mas uma
conta pertence a somente um usuário.
"""

"""
            DICA
Para vincular um usuário a uma conta, filtre a lista de usuários
buscandp o número do CPF informado para cada usuário da 
lista.
"""


def criar_usuario():
    pass


def criar_conta_corrente():
    pass


def sacar():
    pass


def deposito():
    pass


def main():
    while True:
        print("======================= MENU =======================")
        escolha = int(input("[1] Depositar \n[2] Sacar \n[3] Extrato \n[0] Sair \n"
                            "====================================================\n"))
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 0:
            break
        else:
            print("Erro, informe um número existente no menu")


main()
