import textwrap


def menu():
    menu_text = """\n
    ===============Escolha uma das opções=====================
       [1]\tDepositar
       [2]\tSacar
       [3]\tExtrato
       [4]\tNova conta
       [5]\tListar Contas
       [6]\tNovo Usuário
       [0]\tSair
    =>: """
    return input(textwrap.dedent(menu_text))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: +{valor:.2f}")
        print("Transação concluída com sucesso")
    else:
        print("\nOcorreu um erro tente novamente")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Voce não pode realizar essa operação.\n Voce nao tem saldo suficiente")
    if excedeu_limite:
        print("Limite de saques excedido")
    if excedeu_saques:
        print("Voce ultrapassou o limite diario de saque")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque{valor:.2f}"
        numero_saques += 1
    else:
        print("Ocorreu um erro!!")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF do novo usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Digite o nome do novo usuário: ")
    data_nascimento = input("Data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe seu Estado: ")
    usuarios.append({"nome": nome, "cpf": cpf,
                    "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nOcorreu um erro:(")


def listar_contas(contas):
    print("Lista de Contas:")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("Quanto deseja depositar? "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            
            valor = float(input("Quanto deseja sacar? "))
            
            sacar(saldo=saldo, valor=valor, extrato=extrato,
                  limite=limite, numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES,)
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)
                
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "0":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()
