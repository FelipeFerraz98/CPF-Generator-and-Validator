from algorithm_validator import algorithm_validator # Importa a função algorithm_validator do módulo algorithm_validator
from algorithm_generator import algorithm_generator # # Importa a função algorithm_generator do módulo algorithm_generator
import manager # Importa o módulo manager
import time # Importa biblioteca time


# Função que entrega as configurações para o usuário e logo após chama função algorithm_generator
def cpf_generator(): 
    cpf_list = [] # Lista de CPFS gerados
    while True:
        cpf = algorithm_generator() # Chama função algorithm_generator
        print(f'\nO CPF gerado foi: {cpf}') # Imprime o resultado da função, CPF

        save = input("\nDeseja salvar o CPF? (S/N): ") # Pergunta ao usuário se deseja salvar o CPF gerado
        save = save.upper() # Converte a resposta em caixa alta

        if save == 'S': 
            cpf_list.append(cpf) # Em caso de escolha 'S' salva o CPF na lista

        choice = input("\nDeseja gerar um novo CPF? (S/N):") # Pergunta ao usuário se deseja gerar um novo CPF
        choice = choice.upper() # Converte a resposta em caixa alta

        if choice == 'N': # Em caso de escolha 'N' sai do gerador

            if len(cpf_list) >= 1: # Caso haja CPF na lista de cpfs para salvar
                
                archive = input('Digite um nome para o arquivo para salvar os CPFs: ') + '.json' # Pergunta ao usuário o nome do arquivo que vai salvar
                manager.save_json(archive, cpf_list) # Chama módulo manager e função save_json para salvar os CPFs em um json
            
            print("\nObrigado por utilizar o gerador de CPF\n") # Mensagem de fechamento do gerador
            break # Fecha o gerador de CPF


# Função que entrega as configurações para o usuário e logo após chama função algorithm_generator
def cpf_validator():
    cpf_list = []
    while True:
        try:
            cpf_list.clear()
            choice = 0
            choice = int(input('''Digite uma opção:

            [1] Inserir CPF para validar
            [2] Inserir um arquivo com CPFs para validar
            [3] Sair do validador
            
            Digite sua escolha: '''))

            if choice == 1:
                program_continue = 'S'
                while program_continue == 'S':
                    cpf = input('Digite o CPF: ')
                    cpf_list.append(cpf)
                    program_continue = input('Deseja inserar outro CPF? (S/N): ')
                    program_continue = program_continue.upper()
                for cpf in cpf_list:
                    if algorithm_validator(cpf):
                        print(f'CPF {cpf} É VÁLIDO!')
                    else:
                        print(f'CPF {cpf} É INVALIDO!')

            elif choice == 2:
                archive = manager.search_json()
                dados = manager.read_json(archive)
                for cpf in dados:
                    if algorithm_validator(cpf):
                        print(f'CPF {cpf} É VÁLIDO!')
                    else:
                        print(f'CPF {cpf} É INVALIDO!')
                        
                time.sleep(3)

            else:
                print("\nObrigado por utilizar o validador de CPF\n")
                break

        except ValueError:
            print('Digite uma opção válida!') 


def cpf_search():
    cpf_list = []
    while True:
        try:
            choice = int(input('''Digite uma opção:

            [1] Salvar CPF manualmente
            [2] Buscar CPF
            [3] Sair do gerenciador
            
            Digite sua escolha: '''))

            if choice == 1:
                program_continue = 'S'
                archive = input('Digite um nome para o arquivo: ') + '.json'
                while program_continue == 'S':
                    cpf = input('Digite o CPF: ')
                    cpf_list.append(cpf)
                    program_continue = input('Deseja inserar um novo CPF? (S/N): ')
                    program_continue = program_continue.upper()

                manager.save_json(archive, cpf_list)

            elif choice == 2:
                archive = manager.buscador_json()
                dados = manager.ler_json(archive)
                print('\nCPF do arquivo:')
                for CPF in dados:
                    print(CPF)
                print()
                time.sleep(3)

            else:
                print("\nObrigado por utilizar o gerenciador de CPF\n")
                break

        except ValueError:
            print('Digite uma opção válida!') 



while True:
    try:
        choice = int(input('''Digite uma opção:

        [1] Gerador de CPFs
        [2] Validador de CPFs
        [3] Gerenciador de CPFs
        [4] Fechar o programa

        Digite sua escolha: '''))

        if choice == 1:
            cpf_generator()

        elif choice == 2:
            cpf_validator()

        elif choice == 3:
            cpf_search()
        
        else:
            print('Obrigado por utilizar o programa!')
            break

    except ValueError:
        print('Digite um valor válido!')