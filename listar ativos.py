def procurar_ativos(dict_ativos):

    try:
        print('\n1. Nome/hostname')
        print('2. ID')

        opcao = input('Buscar ativo por nome/hostname ou por ID?: ').strip()

        if opcao == '':
            print('\nO campo não pode estar vazio!')
            return False

        if opcao == '1':
            hostname = input('Digite o nome/hostname do ativo: ').strip()

            if hostname == '':
                print('\nO campo não pode estar vazio!')
                return False

            if hostname.isdigit():
                print('\nO nome/hostname não pode ser apenas números!')
                return False

            encontrados = {
                id_ativo: dados
                for id_ativo, dados in dict_ativos.items()
                if dados['hostname'].lower() == hostname.lower()
            }

            if not encontrados:
                print(f'\nO ativo "{hostname}" não está cadastrado no sistema!')
                return False

            for id_ativo, dados in encontrados.items():
                _exibir_ativo(id_ativo, dados)
            return True

        elif opcao == '2':
            id_ativo = input('Digite o ID do ativo que deseja buscar: ').strip()

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

            _exibir_ativo(id_ativo, dict_ativos[id_ativo])
            return True

        else:
            print('\nOpção inválida! Digite 1 para buscar por nome/hostname, ou 2 para buscar por ID.')
            return False

    except KeyboardInterrupt:
        print('\nProcesso encerrado abruptamente pelo usuário. Preparando para encerrar o programa.')
        return False

    except EOFError:
        print('\nNenhuma entrada detectada. Encerrando...')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo {e}')
        return False


def _exibir_ativo(id_ativo, dados):
    """Exibe os dados de um ativo de forma organizada na tela."""
    print('\n' + '=' * 40)
    print(f'ID: {id_ativo}')
    print(f'Hostname/Nome: {dados["hostname"]}')
    print(f'Responsável: {dados["resp"]}')
    print(f'Localização/Setor: {dados["local"]}')
    print(f'Tipo de ativo: {dados["tipo"]}')

    vulns = dados.get('vulnerabilidades', [])
    if vulns:
        print(f'Vulnerabilidades associadas: {len(vulns)}')
        for i, v in enumerate(vulns, start=1):
            print(f'  {i}. {v.get("descricao", "Sem descrição")} '
                  f'(Severidade: {v.get("severidade", "N/A")}, '
                  f'Status: {v.get("status", "N/A")})')
    else:
        print('Vulnerabilidades associadas: nenhuma registrada.')

    print('=' * 40)