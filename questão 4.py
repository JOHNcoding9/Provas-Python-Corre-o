#elabore um script em linguagem Python que leia e valide (não é necessário
#armazená-las) as seguintes informações de cada candidato à vaga de programador na
#empresa Cobra S.A.: Nome: deve ser maior que 3 caracteres; Idade: deve ser entre 0 e
#150; Pretensão Salarial: deve ser maior que zero; Sexo: deve ser 'f' ou 'm'; Estado Civil:
#deve ser 's', 'c', 'v' ou 'd'; O script deve parar de validar (sair do loop) quando o nome
#informado for a palavra: “Sair”. Considerar letras maiúsculas e minúsculas nas
#verificações.

while True: #laço de repetição criado
    try:
        nome=str(input("informe seu nome: ")).strip()# o comando .strip() vai remover qualquer barra de espaço dada pelo usuário
        if len(nome)<3: #verificação se o nome é maior que 3 letras
            print("nome menor que 3 letras")
        if nome.title()=="Sair": #condição que vai quebrar o laço de repetição (escrever "Sair" no input da variavel nome)
            print("encerrando ...")
            break
        idade=int(input("informe sua idade : "))
        if not (0 <= idade < 150): #caso a idade seja menor que 0 e maior que 150 exibir mensagem de invalidez
            print("idade inválida")     
        pretensao=float(input("pretensão salarial: "))
        if pretensao<=0: #pretensão deve ser maior do que zero, se for menor exibirá mensagem de invalidez
            print("pretensão de salário inválida")
        sexo=str(input(" sexo [M/F] ? "))
        if sexo.upper() not in "MF": #verificação se a varivael sexo não contem M de masculino ou F de feminino como valor
            print("sexo inválido")
        estado=str(input("seu estado civil: [s,c,v,d] "))
        if estado.lower() not in "scvd": #verificação se a varivael estado não contem S de solteeiro C de casado, v/viuvo,d/divorciado como valor
            print("estado civil desconhecido/inválido")
    except ValueError as e: #exibição de aviso em caso de erro ao digitar os valores
        print(f"caractere inválido: {e}")