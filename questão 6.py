#uma empresa de viagens e lazer está organizando pacotes de viagens para
#assistir à final de Roland Garros no próximo domingo. Você foi contratado para
#desenvolver um script em linguagem Python que leia e armazene em um dicionário o
#nome, CPF, tipo de acomodação (considerar que serão duas diárias), e o setor da
#quadra que cada pessoa pretende adquirir (“Sair” como nome de pessoa, encerra a
#leitura). O script deve informar o custo total para cada passageiro de acordo com as
#informações a seguir.
#Passagem aérea: US$ 1,450.00
#Acomodações: quarto duplo US$ 240.00 (a diária) ou quarto triplo US$ 180.00 (a
#diária)
#Ingressos: Setor A US$ 800,00 ou Setor B US$ 650,00
#Use um dicionário para armazenar os dados, cada valor do dicionário deverá ser uma
#lista com as informações de cada cliente.
clientes = {}
cod = 1
while True:
 nome = input ("Qual o seu nome ('Sair' - encerra): ").strip()
 if nome.title() == "Sair":
  print("saindo ...")
  break
 cpf = input("Digite seu CPF: ")
 acomodacao = input("Acomodação: 1- (quarto duplo) ou 2-(quarto triplo): ")
 setor = input("Qual setor você irá ficar, A ou B: ")
 dados = [] #toda a vez que eu quero armazenar mais de uma valor em uma mesma chave, eu posso criar uma lista dentro do cicionário ou outro dicionario dentro do primeiro
 dados.append(nome.title())
 dados.append(cpf)
 dados.append(acomodacao)
 dados.append(setor)
 clientes.update ({cod : dados})
 if acomodacao == '1':
  subtotal = 240 * 2
 else:
  subtotal = 180 * 2
 if setor.upper() == "A":
  setor_valor = 800
 else:
  setor_valor = 650
 total_cliente = 1450 + subtotal + setor_valor 
 print(f"{nome.title()}, total US$ {total_cliente:,.2f}")
 cod += 1