#Uma empresa Metalúrgica da cidade está com um programa de coleta e
#reciclagem de aço em andamento. Para tanto, ela precisa que você desenvolva um script
#em linguagem Python que leia e armazene em uma lista a quantidade (em toneladas)
#de sobras de cada mês do ano. Após isto, verifique e mostre o mês ou meses (por
#extenso) que foi realizada a maior coleta. Utilizar um dicionário para armazenar os
#meses por extenso: 1 – Janeiro, 2 – Fevereiro, ...

meses= {1:"Janeiro", 2:"Fevereiro", 3:"Março",
4:"Abril",
5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto",
9:"Setembro", 10:"Outubro", 11:"Novembro",
12:"Dezembro"} #relação de meses por extenso e seus respectivos números

coletas=[] #lista que armazenará a quantidade de toneladas em cada mês
i=1
while i<=12: #variável i assumirá um novo valor de 1 até 12 (respresentantes dos meses no dicionário) em cada nova repetição do bloco de código
    try:
        toneladas=float(input(f"digite a quantidade de toneladas coletadas no mês de {meses[i]}: "))
        coletas.append(toneladas)
        i+=1
    except ValueError: #caso haja um erro no valor de toneladas informadas
        print("quantidade inválida")
maior=max(coletas) # define o maior sendo igual ao valor maximo da lista coletas
for i in range(12): # variavel i assumirá valores de 1 a 12 a cada nova repetição
    if coletas[i]==maior: #caso o valor que a variável i assumir levar para um valor da lista "coletas" que seja igual ao maior
        print(f"A maior quantidade foi {coletas[i]}T no mês {meses[i+1]}") #para cada mês com um valor maior e igual, a seguinte mensagem aparecerá