def listar_vulnerabilidades(dict_ativos):

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

        print(f'\nAtivo: {dict_ativos[id_ativo]["hostname"]} (ID: {id_ativo})')

        if not vulns:
            print('Este ativo está sem vulnerabilidades registradas.')
            return True

        print(f'Vulnerabilidades associadas ({len(vulns)}):')
        print('-' * 40)

        for i, v in enumerate(vulns, start=1):
            print(f'{i}. Descrição: {v["descricao"]}')
            print(f'{i}. Categoria: {v["categoria"]}')
            print(f'{i}. Severidade: {v["severidade"]}')
            print(f'{i}. Status: {v["status"]}')
            print('-' * 40)

        return True

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário. Preparando para encerrar...')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompido.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro inesperado do tipo: {e}')
        return False