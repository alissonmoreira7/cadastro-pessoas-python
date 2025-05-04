
def menu():
    print('-'*30)
    print(' '*6, 'MENU PRINCIPAL')
    print('-'*30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*30)

pessoas = list()
while True:
    menu()
    opcao = int(input('Sua opção: '))

    #ver pessoas cadastradas
    if opcao == 1:
        print(f'O número de pessoas cadastradas é {len(pessoas)}')
        print('As pessoas cadastradas são:', ', '.join(pessoas))
        

    #cadastrar nova pessoa
    if opcao == 2:
        while True:
            person = input('Digite o nome da pessoa: ')
            pessoas.append(person)

            continuar = input('Você deseja continuar? [S/N] ').lower().strip()
            if continuar != 's':
                break

    if opcao == 3:
        print('Saindo do programa...')
        break
