#programa para gerenciamento de pessoas - cadastro de funcionários

#-------inicio da função cadastrar_colaborador()-------
def cadastrar_colaborador(id_global):
    print('*'*70)
    print('-'*20, "MENU CADASTRAR COLABORADOR(A)", '-'*20)
    #global lista_colaboradores
    colaborador = {} #cria um dicionário para adicionar as informações de cada colaborador(a) cadastrado(a)
    colaborador['id'] = id_global
    colaborador['nome'] = input('Por favor, digite o nome do(a) colaborador(a): ')
    colaborador['setor'] = input('Por favor, digite o setor do(a) colaborador(a): ')
    colaborador['salario'] = float(input('Por favor, informe o salário do(a) colaborador(a): '))
    lista_colaboradores.append(colaborador.copy()) #copia o dicionário criado dentro da lista
    
#-------inicio da função consultar_colaborador()-------
def consultar_colaborador():
    while True:
        print('*'*70)
        print('-'*20, "MENU CONSULTAR COLABORADOR(A)", '-'*20)
        opcao = input('''
Escolha a opção desejada: 
1-Consultar todas(os)
2-Consultar por Id
3-Consultar por Setor
4-Retornar ao menu
>>> ''')
        if lista_colaboradores == []:
            print('Não há colaboradores(as) cadastrados(as).') #mensagem para caso nenhum colaborador(a) tenha sido cadastrado(a)
            break
        elif opcao not in '1234': #caso o usuário não escolha nenhuma das opções disponíveis
            print('Digite uma opção válida.')
            continue
        elif opcao == '1':
            for colaboradores in lista_colaboradores: #for para varrer cada colaborador da lista
                print('-'*20)
                for keys, valores in colaboradores.items(): #for para varrer cada item dos dicionários
                    print(f'{keys}: {valores}')
                print('-'*20)
            continue
        elif opcao == '2':
            op = int(input('Digite o Id do(a) Colaborador(a): '))
            for colaboradores in lista_colaboradores:
                if colaboradores['id'] == op: #procura pelo colaborador do id indicado pelo usuário
                    print('-'*20)
                    for keys, valores in colaboradores.items():
                        print(f'{keys}: {valores}')
                print('-'*20)
            continue
                
        elif opcao == '3':
            op = input('Digite o setor do(a) Colaborador(a): ')
            for colaboradores in lista_colaboradores:
                if colaboradores['setor'] == op: #procura pelos colaboradores do setor indicado pelo usuário
                    print('-'*20)
                    for keys, valores in colaboradores.items():
                        print(f'{keys}: {valores}')
                print('-'*20)
            continue
        else:
            return #sai da função consultar_colaborador e retorna ao menu principal

#-------inicio da função remover_colaborador()-------
def remover_colaborador():
    while True:
        print('*'*70)
        print('-'*20, "MENU REMOVER COLABORADOR(A)", '-'*20)
        if lista_colaboradores == []:
            print('Não há colaboradores(as) cadastrados(as).') #mensagem para caso nenhum colaborador tenha sido cadastrado
            break
        op = int(input('Digite o id do(a) Colaborador(a) a ser removido(a): '))
        try:
            del lista_colaboradores[op-1]
            print('O(a) colaborador(a) foi removido(a) do cadastro.')
            break
        except ValueError: #tratamento de erro para caso o usuário não digite um valor numérico inteiro
            print('Você digitou um valor não numérico.')
            print('Por favor, digite um número de id válido.')
            continue
        except IndexError: #tratamento de erro para caso o usuário digite um id que não exista no cadastro
            print('Não existe Colaborador(a) registrado(a) com esse id. Digite um id válido.')
            continue
        
#programa principal-----
print('Bem-vinda(o) ao Controle de Colaboradores(as) da Amanda de Lima Santana!')

###variáveis globais
id = 0
lista_colaboradores = []
###

while True:
    print('*'*70)
    print('-'*27, "MENU PRINCIPAL", '-'*27)
    opcao = input('''Escolha a opção desejada: 
1-Cadastrar Colaborador(a)
2-Consultar Colaborador(es/as)
3-Remover Colaborador(a)
4-Sair
>>> ''')
    
    if opcao not in '1234':
        print('Opção inválida. Digite novamente.')
        continue
    elif opcao == '1':
        id += 1
        cadastrar_colaborador(id)
        continue
    elif opcao == '2':
        consultar_colaborador() 
    elif opcao == '3':
        remover_colaborador()
    else:
        break