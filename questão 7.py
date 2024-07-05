#armazene em um dicionário o nome e quantidade de kilos de peixe que os pescadores obtiveram. sabendo que o acima de 80 kilos há uma multa de 3.56 por kilo a mais
#o programa , ao final de armazenar todos os pescadores no dicionário, deve comparar e exibir nome e quantidade de multa para cada em caso de excesso
dicionario={}
quantidade=int(input("quantidade de pescadores a serem analisados: "))
for i in range(quantidade):
    nome=str(input("Nome do pescador: "))
    kilos=float(input("quantidade de peixe (kg): "))
    dicionario[i]= {nome:kilos}
for nome,kilos in dicionario.items():
    excesso = kilos - 80
    if excesso > 0:
        multa = excesso * 3.56
        print(f"O pescador {nome} excedeu a quantidade de kilos de peixe em {excesso:.2f} kg e receberá uma multa de R${multa:.2f}.")