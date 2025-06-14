def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar conta de usuário
[c] Criar conta em agencia
[q] Sair

=> """
    return menu 

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if saldo <= 0:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Valor de saque muito alto.")
    elif numero_saques > LIMITE_SAQUES:
        print("Limite de saques diários atingidos.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato
    
def Depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor de Depósito inválido.")
    
    return saldo, extrato

def Exibir_extrato(saldo, /, *,extrato):
    if len(extrato) > 0:
        print(f"Saldo da conta: {saldo}\n{extrato}")
    else:
        print("Nenhuma operação realizada na conta.")
        
def verifica_usuario_existente(cpf, usuarios):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None

        
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    
    usuario = verifica_usuario_existente(cpf, usuarios)
    
    if usuario:
        print("Usuário já posssui um cadastro")
        return
    
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe o seu endereço: ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    
    print("Usuário criado com sucesso")

def criar_contas(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = verifica_usuario_existente(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado. ")
    
        
        
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 1
    usuarios = []
    Contas = []
    
    while True:
        opcao = input(menu())

        if opcao == "d":
            print("\nDepósito")
            valor_deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = Depositar(saldo, valor_deposito, extrato)
        
        elif opcao == "s":
            print("\nSaque")
            valor_saque = float(input("Valor do Saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    
        elif opcao == "e":
            Exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "u":
            print("Criar conta de usuário:")
            criar_usuario(usuarios)
        
        elif opcao == "c":
            print("Criar conta em agência:")
            Contas.append(criar_contas(AGENCIA, numero_conta, usuarios))
            numero_conta += 1
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()