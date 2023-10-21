# Início das Variáveis Globais
listaPeca = []
codigoPeca = 0


# Fim das Variáveis Globais

# Início da função cadastrarPeca
def cadastrarPeca(codigo):
    print("\n----- Cadastrar Peça ----- ")
    print("Código da peça: {}" .format(codigo))
    nome = input('Digite o NOME da peça: ')
    fabricante = input('Digite o FABRICANTE da peça: ')
    preco = float(input('Digite o PREÇO (R$) da peça: '))
    dicionarioPeca = {'Código'     : codigo,
                      'Nome'       : nome,
                      'Fabricante' : fabricante,
                      'preco'      : preco}
    listaPeca.append(dicionarioPeca.copy())
    print('Peça cadastrada com sucesso!')
# Fim da função cadastrarPeca

# Início da função consultarPeca1
def consultarPeca():
    print("\n----- Consultar Peças -----")
    while True:
        RU4393710 = input('Escolha a opção desejada:\n' + #Identificador como variável
                          '1 - Consultar TODAS as peças\n' +
                          '2 - Consultar peças por CÓDIGO\n' +
                          '3 - Consultar peças por FABRICANTE\n' +
                          '4 - Voltar\n' +
                          '>> ')
        if RU4393710 == '1':
            print('\nListagem de todas as peças:')
            for peca in listaPeca: # Peca vai varrer a lista de peças
                print('--------------------------')
                for key, value in peca.items(): # Varrer todos as key e values do dicionario
                    print('{}: {}' .format(key,value))
            print('--------------------------\n')
        elif RU4393710 == '2':
            print('\nConsulta por Código')
            valorDesejado = int(input("Digite o CÓDIGO desejado: "))
            for peca in listaPeca:
                if peca['Código'] == valorDesejado: # Se o valor do campo codigo for igual ao codigo desejado
                    print('--------------------------')
                    for key, value in peca.items():  # Varrer todos as key e values do dicionario
                        print('{}: {}'.format(key, value))
                    print('--------------------------\n')
        elif RU4393710 == '3':
            print('\nConsulta por Fabricante')
            valorDesejado = input("Digite o nome do Fabricante: ")
            for peca in listaPeca:
                if peca['Fabricante'] == valorDesejado:  # Se o valor do campo fabricante for igual ao valor desejado
                    print('--------------------------')
                    for key, value in peca.items():  # Varrer todos as key e values do dicionario
                        print('{}: {}'.format(key, value))
                    print('--------------------------\n')
        elif RU4393710 == '4':
            return # Retorna ao laço Principal
        else:
            print("\nOpção inválida. Tente novamente.")
            continue # Reinicia o laço Consultar
# Fim da função consultarPeca

# Início da função removerPeca
def removerPeca():
    print("\n ----- Remover Peças -----")
    valorDesejado = int(input("Digite o CÓDIGO da peça a ser removida: "))
    for peca in listaPeca:
        if peca['Código'] == valorDesejado:  # Se o valor do campo codigo for igual ao codigo desejado para remover
            listaPeca.remove(peca)
            print("Produto removido com sucesso!")
# Fim da função removerPeca

#Programa Principal
print("Seja bem-vindo(a) ao Controle de Estoque de Maluche Bikes")
while True:
    menuPrincipal = input('\nEscolha a opção desejada:\n' +
                          '1 - Cadastrar Peça\n' +
                          '2 - Consultar Peça\n' +
                          '3 - Remover Peça\n' +
                          '4 - Sair\n' +
                          '>> ')
    if menuPrincipal == '1':
        codigoPeca += 1
        cadastrarPeca(codigoPeca)
    elif menuPrincipal == '2':
        consultarPeca()
    elif menuPrincipal == '3':
        removerPeca()
    elif menuPrincipal == '4':
        print("Encerrando o programa. . .")
        break # Finaliza o laço Principal
    else:
        print("\nOpção inválida. Tente novamente.")
        continue # Reinicia o laço Principal