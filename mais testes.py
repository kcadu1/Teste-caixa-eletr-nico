saldo = 100
x = 0

while x != 4:
    
    def saque(saldo):
        try:
            valor = float(input("quanto sacar: "))
            if valor <= float(saldo):
                saldo -= valor
                print(f"valor sacado: {valor}")
                print(f"saldo apos saque: {saldo}")
            else: print("vai se fuder, caloteiro")
        except ValueError:
            print("nao numero")
        return saldo
    
    def depositar(saldo):
        try: 
            valor = float(input("quanto depositar: "))
            saldo += valor
            print(f"saldo novo: {saldo}")
        except ValueError:
            print("nao numero")
        return saldo
        
    def extrato(saldo):
        print(f"extrato: {saldo}")
    try:
        x = int(input("opcao: \n 1 - sacar \n 2 - depositar \n 3 - extrato \n 4 - sair \n" ))
        if x == 1:
            saldo=saque(saldo)

        if x == 2:
            saldo=depositar(saldo)

        if x == 3:
            extrato(saldo)
    except ValueError:
            print("nao numero")