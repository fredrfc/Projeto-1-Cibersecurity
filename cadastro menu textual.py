def cadastro_ativo_menu(dict_ativos, caminho_arquivo='arquivo.json'):
    try:
        id_ativo = input('Qual é o ID do novo ativo? (Deve ser um número inteiro positivo e válido): ').strip()

        if id_ativo == '':
            print('\nErro! O campo não pode estar vazio!')
            return False

        if not id_ativo.isdigit():
            print('\nErro! O ID deve ser um número inteiro positivo e válido!')
            return False

        id_ativo = int(id_ativo)

        if id_ativo in dict_ativos:
            print('\nO ID digitado já está cadastrado no sistema.')
            return False

        hostname = input('Qual é o nome/hostname do ativo?: ').strip()
        resp = input('Quem é o responsável técnico pelo ativo?: ').strip()
        local = input('Qual é a localização/setor do ativo?: ').strip()
        tipo = input('Qual é o tipo do ativo?: ').strip()

        if hostname == '' or resp == '' or local == '' or tipo == '':
            print('\nO(s) campo(s) não pode(m) estar vazio(s)!')
            return False
        
        dict_ativos[id_ativo] = {
            'hostname': hostname,
            'resp': resp,
            'local': local,
            'tipo': tipo,
            'vulnerabilidades': []
        }

        return _salvar_arquivo(dict_ativos, caminho_arquivo, hostname)

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário. Preparando para encerrar o programa.')
        return False

    except EOFError:
        print('\nProcesso de entrada de dados interrompida.')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False
