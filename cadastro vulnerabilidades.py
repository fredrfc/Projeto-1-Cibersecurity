SEVERIDADES_VALIDAS = ['baixa', 'media', 'alta', 'critica']
STATUS_VALIDOS = ['aberta', 'em tratamento', 'corrigida', 'aceita como risco']


def cadastrar_vulnerabilidade(dict_ativos, caminho_arquivo='arquivo.json'):

    try:
        id_ativo = input('Digite o ID do ativo para associar a vulnerabilidade: ').strip()

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

        print('\nAtivo selecionado:')
        _exibir_ativo(id_ativo, dict_ativos[id_ativo])

        descricao = input('\nDescrição da vulnerabilidade: ').strip()
        if descricao == '':
            print('\nA descrição não pode estar vazia!')
            return False

        categoria = input('Categoria/tipo da vulnerabilidade (ex: senha fraca, software desatualizado): ').strip()
        if categoria == '':
            print('\nA categoria não pode estar vazia!')
            return False

        print(f'\nSeveridades válidas: {", ".join(SEVERIDADES_VALIDAS)}')
        severidade = input('Severidade: ').strip().lower()

        if severidade not in SEVERIDADES_VALIDAS:
            print(f'\nSeveridade inválida! Escolha entre: {", ".join(SEVERIDADES_VALIDAS)}')
            return False

        print(f'\nStatus válidos: {", ".join(STATUS_VALIDOS)}')
        status = input('Status de tratamento: ').strip().lower()

        if status not in STATUS_VALIDOS:
            print(f'\nStatus inválido! Escolha entre: {", ".join(STATUS_VALIDOS)}')
            return False

        nova_vulnerabilidade = {
            'descricao': descricao,
            'categoria': categoria,
            'severidade': severidade,
            'status': status
        }

        dict_ativos[id_ativo]['vulnerabilidades'].append(nova_vulnerabilidade)

        sucesso = _salvar_arquivo(dict_ativos, caminho_arquivo)

        if sucesso:
            print(f'\nVulnerabilidade cadastrada com sucesso no ativo {id_ativo}!')
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