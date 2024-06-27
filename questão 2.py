#utilize um dicionário para armazenar o cardápio de uma lanchonete. Para
#cada item do cardápio devem ser armazenados a descrição, o código e o preço. Itens:
#Cachorro-Quente. 100. R$ 8,20,
#Bauru Simples. 101. R$ 9,30,
#Bauru com ovos. 102. R$ 1,50,
#Hambúrguer. 103. R$ 11,20,
#Cheeseburguer. 104. R$ 14,30,
#Refrigerante Lata. 105. R$ 5,00.
#Desenvolva um script em linguagem Python que leia o código dos itens dos pedidos e as
#quantidades desejadas em loop até que o cliente decida terminar a compra (informando
#0). Calcule e mostre o valor a ser pago por item e o total geral do pedido. O script deve
#permitir pedidos de outros clientes até que o “expediente” seja fechado, ou seja, mesmo
#após o término do primeiro pedido, o script deve continuar rodando para receber mais
#pedidos.

cardapio={ 100:["Cachorro quente",8.20], # Cardápio em si
          101:["Bauru simples",9.30],
          102:["Bauru com ovos",1.50],
          103:["Burguer",11.20],
          104:["CheeseBurguer",14.30],
          105:["refrigerante quente 2L",5]}
total_geral=0 #total_geral representa o lucro do restaurante neste dia, juntando o gasto de todos os clientes em seu restaurante
while True: #enquanto while true não for quebrado por um "break" o total do cliente se reineciará a cada cliente novo
    total=0 # total gasto pelo cliente
    while True: #enquanto não for quebrado por um break, o cliente escolherá quantos e qual a quantidade de itens ele quiser
        try:
            cod=int(input("digite o código do produto (digite 0 para sair): "))
            if cod in cardapio:
                try:
                    quantidade=int(input(f"quantidade de {cardapio[cod][0]} desejada:  "))
                    valor_item=quantidade*cardapio[cod][1] #o valor_item será a quantidade escolhida pelo usuário vezes o valor contido na posição 1 da lista contida no dicionário cardapio
                    total=total+valor_item #o total do cliente será acrescido com o valor de cada item novo que o usuário quiser
                    print(f"total do item em R$: {valor_item:,.2f}")# o comando :,.2f arredonda o número em questão para apenas 2 casas decimais
                except ValueError: # em casos de erro em selecionar uma quantidade válida, o seguinte recado aparecerá
                    print("quantidade inválida")
            if cod==0: # se o código digitado for igual a zero, será exibido o total gasto por esse cliente e a sua vez se encerrará, dando a vez ao próximo cliente
               print(f"total do cliente R$: {total:,.2f}")
               break
            elif cod not in cardapio: #caso o código inserido não esteja no cardapio, a seguinte mensagem aparece
               print("código inexistente")
        except ValueError: #caso o codigo digitado  possua um erro de valor, a seguinte mensagem aparecerá
         print("código inválido")
    total_geral+=total #o total_geral (lucro do restaurante) é a soma de cada gasto total de cada cliente
    resp=input("deseja fechar o expediente? S/N ") 
    if resp.upper()=='S': #caso o dono do restaurnte deseje fechar o expediente, ele se encerrará com o break e exibirá o lucro do dia do restaurante 
        break
print(f"valor em caixa R$: {total_geral:,.2f}")