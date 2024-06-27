#crie um script em linguagem Python que leia um vetor (lista) A com
# números inteiros, (0 – Zero termina a digitação). Em seguida, o script deve calcular e
#mostrar a soma dos quadrados dos elementos do vetor que estão nos indexes pares
#(incluindo o index 0).


lista_A=[]
import math
while True: #While True é um loop o qual só será quebrado caso haja um "break" para queebrar o looping
 try: #o "try" tentará rodar a linha de código
    num=int(input("digite números inteiros: ")) #aguarda o usuario digitar um numero inteiro
    if num==0: #se o numero digitado pelo usuario for o "0" o looping será quebrado
        break
    lista_A.append(num) # o numero digitado pelo usuário é adicionado a lista_A
 except: # qualquer problema ao tentar rodar a linha de código relacionada ao "try" é substitída pelo código do "except"
    print("número inválido")
 soma=0
 for i in range(0,len(lista_A),2): #a variavel i receberá os valores de um intervalo, com ínício no 0 e fim no index final da lista, marcado por "len(lista_A)". O valor final "2" é atribuido ao modo de contagem desse inervalo, no caso seria um intervalo pulando de 2 em 2.
  soma=soma+math.pow(lista_A[i],2) # realiza a soma do quadrdaos dos indexes pares para cada valor i pulando de 2 em 2 indexes.
 print(soma)
print("o valor  total deu: ", soma)