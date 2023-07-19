"""
Separar as funções existentes de saque, depósito e
extrato em funções. Criar duas novas funções:
cadastrar usuário (cliente) e cadastrar conta bancária.
"""

"""
                    DESAFIO
Precisamos deixar nosso código mais modularizado, para isso 
vamos criar funções para as operações existentes: sacar,
depositar e visualizar histórico. Além disso, para a versão 2 do
nosso sistema precisamos criar duas novas funções: criar
usuário (cliente do banco) e criar conta corrente (vincular com
usuário).
"""

"""
            SEPARAÇÃO EM FUNÇÕES
Devemos criar funções para todas as operações do sistema.
Para exercitar tudo o que aprendemos neste módulo, cada
função vai ter uma regra na passagem de argumentos. O
retorno e a forma como serão chamadas, pode ser definida por
você da forma que char melhor.
"""

"""
            SAQUE
A função saque deve receber os argumentos apenas por nome
(keyword only). Sugestão de argumentos: saldo, valor, extrato,
limite, numero_saques, limites_saques. Sugestão de retorno:
saldo e extrato.
"""

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
