def remover_vulnerabilidade(dict_ativos, caminho_arquivo='arquivo.json'):

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

        escolha = input('\nDigite o número da vulnerabilidade que deseja remover: ').strip()

        if not escolha.isdigit():
            print('\nValor inválido! Digite um número da lista.')
            return False

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(vulns):
            print('\nNúmero fora da lista.')
            return False

        vulnerabilidade = vulns[indice]

        print('\nVocê está prestes a remover:')
        print(f'{vulnerabilidade["descricao"]} (Severidade: {vulnerabilidade["severidade"]}, Status: {vulnerabilidade["status"]})')

        confirmacao = input('\nTem certeza que deseja remover esta vulnerabilidade? Digite [s] para sim ou [n] para não: ').strip().lower()

        if confirmacao != 's':
            print('\nOperação cancelada. Nenhum dado foi removido.')
            return False

        vulns.pop(indice)

        sucesso = _salvar_arquivo(dict_ativos, caminho_arquivo)

        if sucesso:
            print('\nVulnerabilidade removida com sucesso!')
            return True

        return False

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário. Preparando para encerrar...')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompido.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro inesperado do tipo: {e}')
        return False