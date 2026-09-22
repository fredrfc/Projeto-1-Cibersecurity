def atualizar_ativo(dict_ativos, caminho_arquivo='arquivo.json'):

    try:
        id_ativo = input('\nDigite o ID do ativo que deseja atualizar: ').strip()

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

        print('\nDados atuais do ativo:')
        exibir_ativo(id_ativo, dict_ativos[id_ativo])

        print('\nDigite o novo valor para cada informação, ou deixe em branco para manter o valor atual.')

        hostname_novo = input(f'Hostname/Nome [{dict_ativos[id_ativo]["hostname"]}]: ').strip()
        resp_novo = input(f'Responsável [{dict_ativos[id_ativo]["resp"]}]: ').strip()
        local_novo = input(f'Localização/Setor [{dict_ativos[id_ativo]["local"]}]: ').strip()
        tipo_novo = input(f'Tipo de ativo [{dict_ativos[id_ativo]["tipo"]}]: ').strip()

        if hostname_novo == '' and resp_novo == '' and local_novo == '' and tipo_novo == '':
            print('\nNenhuma alteração foi feita.')
            return False

        if hostname_novo != '':
            dict_ativos[id_ativo]['hostname'] = hostname_novo

        if resp_novo != '':
            dict_ativos[id_ativo]['resp'] = resp_novo

        if local_novo != '':
            dict_ativos[id_ativo]['local'] = local_novo

        if tipo_novo != '':
            dict_ativos[id_ativo]['tipo'] = tipo_novo

        sucesso = _salvar_arquivo(dict_ativos, caminho_arquivo)

        if sucesso:
            print(f'\nAtivo {id_ativo} atualizado com sucesso!')
            _exibir_ativo(id_ativo, dict_ativos[id_ativo])
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