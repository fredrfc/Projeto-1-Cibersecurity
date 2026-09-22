def atualizar_vulnerabilidade(dict_ativos, caminho_arquivo='arquivo.json'):

    try:
        id_ativo = input('Digite o ID do ativo: ').strip()

        if id_ativo == '':
            print('\nO campo não pode estar vazio!')
            return False

        if not id_ativo.isdigit():
            print('\nO ID não pode conter letras, apenas números inteiros e positivos!')
            return False

        id_ativo = int(id_ativo)

        if id_ativo not in dict_ativos:
            print(f'\nNão existe um ativo com o ID {id_ativo} cadastrado no sistema!')
            return False

        vulns = dict_ativos[id_ativo].get('vulnerabilidades', [])

        if not vulns:
            print(f'\nO ativo {id_ativo} não possui vulnerabilidades registradas.')
            return False

        print(f'\nVulnerabilidades do ativo {id_ativo}:')
        for i, v in enumerate(vulns, start=1):
            print(f'{i}. {v["descricao"]} (Severidade: {v["severidade"]}, Status: {v["status"]})')

        escolha = input('\nDigite o número da vulnerabilidade que deseja atualizar: ').strip()

        if not escolha.isdigit():
            print('\nValor inválido! Digite um número da lista.')
            return False

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(vulns):
            print('\nNúmero fora da lista.')
            return False

        vulnerabilidade = vulns[indice]

        print('\nDados atuais da vulnerabilidade:')
        print(f'Descrição: {vulnerabilidade["descricao"]}')
        print(f'Categoria: {vulnerabilidade["categoria"]}')
        print(f'Severidade: {vulnerabilidade["severidade"]}')
        print(f'Status: {vulnerabilidade["status"]}')

        print('\nDigite o novo valor para cada informação, ou deixe em branco para manter o valor atual.')

        descricao_nova = input(f'Descrição [{vulnerabilidade["descricao"]}]: ').strip()
        categoria_nova = input(f'Categoria [{vulnerabilidade["categoria"]}]: ').strip()

        print(f'Severidades válidas: {", ".join(SEVERIDADES_VALIDAS)}')
        severidade_nova = input(f'Severidade [{vulnerabilidade["severidade"]}]: ').strip().lower()

        if severidade_nova != '' and severidade_nova not in SEVERIDADES_VALIDAS:
            print(f'\nSeveridade inválida! Escolha entre: {", ".join(SEVERIDADES_VALIDAS)}')
            return False

        print(f'Status válidos: {", ".join(STATUS_VALIDOS)}')
        status_novo = input(f'Status [{vulnerabilidade["status"]}]: ').strip().lower()

        if status_novo != '' and status_novo not in STATUS_VALIDOS:
            print(f'\nStatus inválido! Escolha entre: {", ".join(STATUS_VALIDOS)}')
            return False

        if (descricao_nova == '' and categoria_nova == '' and severidade_nova == '' and status_novo == ''):
            print('\nNenhuma alteração foi feita.')
            return False

        if descricao_nova != '':
            vulnerabilidade['descricao'] = descricao_nova

        if categoria_nova != '':
            vulnerabilidade['categoria'] = categoria_nova

        if severidade_nova != '':
            vulnerabilidade['severidade'] = severidade_nova

        if status_novo != '':
            vulnerabilidade['status'] = status_novo

        sucesso = _salvar_arquivo(dict_ativos, caminho_arquivo)

        if sucesso:
            print('\nVulnerabilidade atualizada com sucesso!')
            return True

        return False

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário.')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompido.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro inesperado: {e}')
        return False