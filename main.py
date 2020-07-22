import csv

saldo_anterior, credito, cartao, mercado, padaria, farmacia, gastos_casa, uber, outros, pgtos, investimentos = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
total_do_mes = 0.0

def menu(item, gasto):
    print('****'*3 + 'M E N U' + '****'*3)
    print(item)
    print('****'*3 + '*******' + '****'*3)
    print('****'*3 + ' GASTO ' + '****'*3)
    print(gasto)
    print('****'*3 + '*******' + '****'*3)
    print('1   -   Crédito')
    print('2   -   Cartão')
    print('3   -   Mercado')
    print('4   -   Padaria e Ifood')
    print('5   -   Farmácia')
    print('6   -   Gastos de Casa')
    print('7   -   Uber')
    print('8   -   Saldo Anterior')
    print('9   -   outros')
    print('10  -   Pagamentos de emprestimo')
    print('11  -   Investimentos')

def menu_gastos():
    print('****'*3 + ' TOTAL ' + '****'*3)
    print('****'*3 + '*******' + '****'*3)

if __name__ == '__main__':
    with open('extrato.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter=',')
        for gastos in leitor:
            try:
                menu(gastos[2], gastos[5])
                tipo_gasto = int(input('Qual é esse tipo de gasto?'))
                if tipo_gasto == 1:
                    credito += abs(float(gastos[5]))
                    print()
                if tipo_gasto == 2:
                    cartao += abs(float(gastos[5]))
                if tipo_gasto == 3:
                    mercado += abs(float(gastos[5]))
                if tipo_gasto == 4:
                    padaria += abs(float(gastos[5]))
                if tipo_gasto == 5:
                    farmacia += abs(float(gastos[5]))
                if tipo_gasto == 6:
                    gastos_casa += abs(float(gastos[5]))
                if tipo_gasto == 7:
                    uber += abs(float(gastos[5]))
                if tipo_gasto == 8:
                    saldo_anterior += abs(float(gastos[5]))
                if tipo_gasto == 9:
                    outros += abs(float(gastos[5]))
                if tipo_gasto == 10:
                    pgtos += abs(float(gastos[5]))
                if tipo_gasto == 11:
                    investimentos += abs(float(gastos[5]))
                if tipo_gasto == 1000:
                    break
            except:
                print('É uma string')
        total_do_mes = credito - saldo_anterior - cartao - mercado - padaria - farmacia - gastos_casa - uber - outros - pgtos - investimentos
        menu_gastos()
        menu_gastos()
        print(f'{credito}   -   Crédito')
        print(f'{cartao}   -   Cartão')
        print(f'{mercado}   -   Mercado')
        print(f'{padaria}   -   Padaria e Ifood')
        print(f'{farmacia}   -   Farmácia')
        print(f'{gastos_casa}   -   Gastos de Casa')
        print(f'{uber}   -   Uber')
        print(f'{saldo_anterior}   -   Saldo Anterior')
        print(f'{outros}   -   Outros')
        print(f'{pgtos}   -   Pagamentos de emprestimos')
        print(f'{investimentos}   -   Investimentos')
        print('Resultado de sua conta é: {total_do_mes}')
