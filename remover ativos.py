def deletar_ativo(dict_ativos, caminho_arquivo='arquivo.json'):

    try:
        id_ativo = input('Digite o ID do ativo que deseja remover: ').strip()

        if id_ativo == '':
            print('\nO campo não pode estar vazio!')
            return False

        if not id_ativo.isdigit():
            print('\nO ID não pode conter letras, apenas números inteiros e positivos!')
            return False

        id_ativo = int(id_ativo)

        if id_ativo not in dict_ativos:
            print(f'\nNão existe um ativo com o ID: {id_ativo} cadastrado no sistema!')
            return False

        print('\nVocê está prestes a remover o seguinte ativo:')
        _exibir_ativo(id_ativo, dict_ativos[id_ativo])

        qtd_vulns = len(dict_ativos[id_ativo].get('vulnerabilidades', []))
        if qtd_vulns > 0:
            print(f'\nAtenção: {qtd_vulns} vulnerabilidade(s) associada(s) também será(ão) removida(s).')

        confirmacao = input('\nTem certeza que deseja remover este ativo? Digite [s] para sim ou [n] para não: ').strip().lower()

        if confirmacao != 's':
            print('\nOperação cancelada. Nenhum dado foi removido.')
            return False

        del dict_ativos[id_ativo]

        sucesso = _salvar_arquivo(dict_ativos, caminho_arquivo)

        if sucesso:
            print(f'\nAtivo {id_ativo} removido com sucesso!')
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