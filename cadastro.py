def cadastrar_ativo(id_ativo, hostname, resp, local, tipo, dict_ativos, caminho_arquivo='arquivo.json'):
    
    try:
        dict_ativos[id_ativo] = {
            'hostname': hostname,
            'resp': resp,
            'local': local,
            'tipo': tipo,
            'vulnerabilidades': []
        }
        
        id_ativo = (input('Qual é o ID do novo ativo?: ')).strip()

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário. Preparando para encerrar o programa.')

    except EOFError:
        print('\nProcesso de entrada de dados interrompida.')

    except Exception as e:
        print(f'Erro! Ocorreu um erro do tipo: {e}')

        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dict_ativos, f, ensure_ascii=False, indent=4)

        print(f'\nSucesso! Ativo {hostname} foi cadastrado com sucesso no sistema!')
        return True
    
    except PermissionError:
        print('\nErro! O acesso ao arquivo foi negado.')

    except IOError as e:
        print(f'\nErro! Houve um problema na entrada/saída ao salvar o arquivo: {e}')
        return False
    
    except Exception as e:
        print(f'\nErro! Aconteceu um erro inesperado do tipo {e}')
        return False