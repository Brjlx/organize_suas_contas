import csv

saldo_gasto = 0.0

with open('extrato.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for gastos in leitor:
        try:
            saldo_gasto += float(gastos[5])
            print('Somaandooooo', saldo_gasto)
        except:
            print('Esse não deu pra somar  ', gastos[2])

    print(saldo_gasto / 2)
