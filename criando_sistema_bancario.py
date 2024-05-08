def saque(saldo, saques, saques_dia):
    if saques_dia < 3 and saques <= 500:
        saques_dia += 1
        saldo -= saques
        print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    else:
        print('Limite de saques diarios atingido ou valor acima do permitido.')

    return saldo, saques_dia


def deposito(saldo, depositos):
    saldo += depositos
    print(f'Deposito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')

    return saldo


def extrato(saldo, depositos, saques):
    print('Extrato')
    print('-' * 30)
    if len(depositos) == 0 and len(saques) == 0:
        print('Não foram realizadas movimentações')
    else:
        for deposito in depositos:
            print(f'Deposito de R$ {deposito:.2f}')
        for saque in saques:
            print(f'Saque de R$ {saque:.2f}')
    print(f'Saldo disponivel: R$ {saldo:.2f}')
    print('-' * 30)


def main():
    saldo = 0
    depositos = []
    saques = []
    saques_dia = 0

    while True:
        print('1 - Deposito')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Sair')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            depositos.append(float(input('Digite o valor do deposito: ')))
            saldo = deposito(saldo, depositos[-1])
        elif opcao == 2:
            saques.append(float(input('Digite o valor do saque: ')))
            saldo, saques_dia = saque(saldo, saques[-1], saques_dia)
        elif opcao == 3:
            extrato(saldo, depositos, saques)
        elif opcao == 4:
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()
