def _salvar_arquivo(dict_ativos, caminho_arquivo, hostname=None):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dict_ativos, f, ensure_ascii=False, indent=4)
        
        if hostname:
            print(f'\nSucesso! Ativo "{hostname}" cadastrado com sucesso!')
            return True

    except PermissionError:
        print('\nErro! O acesso ao arquivo de base de dados foi negado.')
        return False

    except IOError as e:
        print(f'\nErro! Problema de entrada/saída ao salvar o arquivo: {e}')
        return False
