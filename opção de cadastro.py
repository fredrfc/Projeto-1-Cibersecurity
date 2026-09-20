def menu_cadastro(dict_ativos, caminho_arquivo='arquivo.json'):
    print('\nComo deseja cadastrar o ativo?')
    print('1 - Digitar manualmente as informações')
    print('2 - Importar de um arquivo JSON')
    
    opcao = input('\nQual maneira de cadastro você prefere?: ').strip()

    if opcao == '1':
        cadastrar_por_menu(dict_ativos, caminho_arquivo)
    elif opcao == '2':
        caminho = input('Caminho do arquivo JSON a importar: ').strip()
        cadastrar_por_arquivo(caminho, dict_ativos, caminho_arquivo)
    else:
        print('\nOpção inválida.')