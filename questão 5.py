# desenvolva um script em linguagem Python que receba a temperatura
#média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual
#das temperaturas. Em seguida, o script deve mostrar todas as temperaturas acima da
#média anual e em que mês (por extenso) elas ocorreram (Utilizar um dicionário para
#armazenar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).

ano = {1 : "Janeiro", 2 : "Fevereiro", 3 : "Março", 4 :
"Abril",
5 : "Maio", 6 : "Junho", 7 : "Julho", 8 :
"Agosto",
9 : "Setembro", 10 : "Outubro", 11 : "Novembro",
12 : "Dezembro"} 

temperaturas=[]
try:
 for i in range(1,13):
     temp=float(input(f"digite a temperatura média de {ano[i]}: "))
     temperaturas.append(temp)
except ValueError as e:
   print(f"temperatura invalida : {e}")
try:
 media_anual=sum(temperaturas)/len(temperaturas) # sum() somara todos os valores presentes na lista temperaturas, enquanto len() retornará o "comprimento" de itens da lista
except ZeroDivisionError as y:
 print("não foi possivel calcular a média anual das temperaturas: ", y)
for idx, temperatura in enumerate(temperaturas, start=1): #a variável temperatura assumirá o valor de cada numero presente na lista "temperaturas", enquanto a variavel idx assumirá o índice de cada valor "temperatura" presente na lista "'temperaturas", começando a contagem a a partir de 1 ao invés de 0
        if temperatura > media_anual:
            print(f"Temperatura {temperatura:.2f} no mês de {ano[idx]} está acima da média ({media_anual:.2f})")
