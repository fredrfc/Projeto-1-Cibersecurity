from enum import Enum

class TipoAtivo(Enum):
    NOTEBOOK = 1
    ROTEADOR = 2
    SERVIDOR = 3
    SOFTWARE_LICENCIADO = 4
    BANCO_DE_DADOS = 5

dict_ativos = {}

dict_ativos[id_ativo] = {
    'hostname': hostname,
    'responsavel': resp,
    'setor': setor,
    'tipo': tipo,
    'vulnerabilidades': []
}

while True:
    print('-' * 30)
    print('SISTEMA DE CADASTRO DE ATIVOS')
    print('-' * 30)
    print('1. Visualizar ativos cadastrados no sistema.')
    print('2. Cadastrar novo ativo.')
    print('3. Atualizar ativo.')
    print('4. Remover ativo')
    print('5. Sair.')

    try:
        opcao = input('Digite o número da opção que deseja: ').strip()

    except KeyboardInterrupt:
        print('\nOperação terminada abruptamente pelo usuário. Preparando para encerrar o programa.')
        break

    except EOFError:
        print('\nProcesso de entrada de dados interrompida.')
        break

    except Exception as e:
        print(f'\nErro! Aconteceu um problema inesperado do tipo: {e}') 
        break

    if opcao == '1':
        if not dict_ativos:
            print('Até o momento nenhum ativo foi cadastrado.')
            escolha = input('Gostaria de cadastrar o primeiro ativo do sistema? (Digite [s] para sim e [n] para não): ').strip().lower()
            if escolha == 's':
                #chamar função de cadastro
                pass
            elif escolha == 'n':
                print('Retornando ao menu principal.\n')
            else:
                print('Opção inválida! Digite [s] para sim ou [n] para não!')

    elif opcao == '2':
        #chamar função de cadastro    
        pass
    elif opcao == '3':
        #chamar função de atualização
        pass
    elif opcao == '4':
        #chamar função de remoção
        pass
    elif opcao == '5':
        print('Encerrando o programa... Preparando para sair...')
        break

    else:
        print('Erro! Digite um valor válido (1, 2, 3, 4, ou 5)!')    
