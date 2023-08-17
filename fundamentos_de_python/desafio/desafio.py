#criando simples sistema bancario
def saque(account, transactions, withdrawals_today):
    saque = int(input("Quanto deseja retirar? "))
    if 20 <= saque <= 500:  # Verifica se o saque está entre 20 e 500
        if saque <= account and withdrawals_today < 3:  # Verifica saldo e saques diários
            account -= saque
            withdrawals_today += 1
            transactions.append(f"Saque: -{saque}")
            print("Saque realizado com sucesso")
            print(f"Você possui na sua conta: {account:.2f}")
        else:
            if saque > account:
                print("Saldo insuficiente para o saque.")
            else:
                print("Limite diário de saques atingido (3 saques).")
    else:
        print("O valor de saque deve estar entre 20 e 500.")
    return account, withdrawals_today


def deposito(account, transactions):
    deposito = int(input("Quanto deseja depositar? "))
    account += deposito
    transactions.append(f"Deposito: +{deposito}")
    print("Transação concluída com sucesso")
    print(f"Você possui na sua conta: {account:.2f}")
    return account


def extrato(account, transactions):
    print(f"Seu saldo atual é: R${account:.2f}")
    print("Histórico de transações:")
    for transaction in transactions:
        print(transaction)

    return account


saldo_inicial = 1000
account = saldo_inicial
transactions = []
withdrawals_today = 0
option = -1

while option != 0:
    print("Escolha uma opção")
    option = int(input(
        "[1] sacar\n[2] deposito\n[3] extrato\n[0] sair\nDigite a opção desejada:"))
    if option == 1:
        account, withdrawals_today = saque(
            account, transactions, withdrawals_today)
    elif option == 2:
        account = deposito(account, transactions)
    elif option == 3:
        account = extrato(account, transactions)
    elif option == 0:
        print("Programa encerrado.")
    else:
        print("Opção inválida.")
