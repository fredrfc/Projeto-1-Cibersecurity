import os
import json

def cadastro_ativo_arquivo(caminho_json_entrada, dict_ativos, caminho_arquivo='arquivo.json'):
    try:
        if not os.path.exists(caminho_json_entrada):
            print(f'\nErro! Não foi possível encontrar o arquivo: {caminho_json_entrada}')
            return False

        with open(caminho_json_entrada, 'r', encoding='utf-8') as f:
            ativos_novos = json.load(f)

        if isinstance(ativos_novos, dict):
            ativos_novos = [ativos_novos]
        
        cadastrados = 0
        
        for ativo in ativos_novos:
            campos_obrigatorios = {'id_ativo', 'hostname', 'resp', 'local', 'tipo'}
            
            if not campos_obrigatorios.issubset(ativo.keys()):
                print('Um registro foi ignorado porque faltaram campos obrigatórios.')
                continue

            id_ativo = ativo['id_ativo']

            if id_ativo in dict_ativos:
                print(f'\nID: {id_ativo}, já existe e portanto foi ignorado.')
                continue

            dict_ativos[id_ativo] = {
                'hostname': ativo['hostname'],
                'resp': ativo['resp'],
                'local': ativo['local'],
                'tipo': ativo['tipo'],
                'vulnerabilidades': ativo.get('vulnerabilidades', [])
            }

            cadastrados += 1

        if cadastrados > 0:
            _salvar_arquivo(dict_ativos, caminho_arquivo)
            print(f'\n{cadastrados} ativo(s) importados do arquivo com sucesso!')
            return True

        else:
            print('\nNenhum ativo novo importado.')
            return False

    except json.JSONDecodeError:
        print('\nErro! O arquivo enviado não é do tipo JSON válido!')
        return False

    except PermissionError:
        print('\nErro! Acesso negado ao arquivo!')
        return False

    except Exception as e:
        print(f'\nErro! Ocorreu um erro do tipo: {e}')
        return False