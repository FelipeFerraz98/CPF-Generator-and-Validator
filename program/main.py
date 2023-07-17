from algorithm_validator import AlgorithmValidator # Importa a classe AlgorithmValidator do módulo algorithm_validator
from algorithm_generator import AlgorithmGenerator # # Importa a classe AlgorithmGenerator do módulo algorithm_generator
import manager # Importa o módulo manager
import time # Importa biblioteca time



# Função que entrega as configurações para o usuário e logo após chama função algorithm_generator
def cpf_generator():
    cpf_list = [] # Lista de CPFS gerados
    while True:
        cpf_algorithm = AlgorithmGenerator() # Chama a classe AlgorithmGenerator e atribui na variavel
        cpf = cpf_algorithm.generator # Chama função de gerar cpf
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

def algorithm_validator_return(cpf: str) -> str:
    validator = AlgorithmValidator(cpf).validator # Mandando o CPF para o algorithm_validator
    if validator:
        print(f'CPF {cpf} É VÁLIDO!') # Caso algorithm_validator retorne True
    else:
        print(f'CPF {cpf} É INVALIDO!') # Caso algorithm_validator retorne False


# Função que entrega as configurações para o usuário e logo após chama função algorithm_generator
def cpf_validator():
    cpf_list = [] # Lista de CPFs para validar por inserção manual

    while True:
        try:
            # Limpar a lista de CPFs inseridos manualmente caso o usuário selecione a mesma opção novamente
            cpf_list.clear() 

            # Escolha do usuário
            choice = int(input('''Digite uma opção:

            [1] Inserir CPF para validar
            [2] Inserir um arquivo com CPFs para validar
            [3] Sair do validador
            
            Digite sua escolha: '''))

            # Escolha 1, inserção manual
            if choice == 1:
                program_continue = 'S' # Variavel de controle

                while program_continue == 'S': # Verficar se o While deve continuar

                    cpf = input('Digite o CPF sem pontuação: ') # Inserir CPF
                    # Verifica se foi inserido todos os digitos do CPF
                    if len(cpf) == 11:
                        cpf_list.append(cpf) # Inserir CPFs na lista
                        program_continue = input('Deseja inserar outro CPF? (S/N): ') # Pergunta para continuar loop
                        program_continue = program_continue.upper()
                        
                    # Caso o usuário não insira todos os digitos
                    else:
                        print('O CPF inserido não os 11 digitos de um CPF!')

                # Desempacotando lista    
                for cpf in cpf_list:
                    algorithm_validator_return(cpf) # Verificar se o CPF é válido
                
                # Tempo de espera para o programa continuar após 3 segundos 
                # para assim o usuário visualizar melhor os CPFs
                time.sleep(3) 

            # Escolha 2, buscar arquivo json e verificar CPFs
            elif choice == 2:

                archive = manager.search_json() # Salvando escolha de arquivo JSON recebido da função manager.search_json
                dados = manager.read_json(archive) # Usando a escolha de arquivo acima para salvar o arquivo JSON em dados
                
                # Desempacotando arquivo JSON
                for cpf in dados:
                    algorithm_validator_return(cpf) # Verificar se o CPF é válido

                # Tempo de espera para o programa continuar após 3 segundos 
                # para assim o usuário visualizar melhor os CPFs       
                time.sleep(3) 

            # Caso de escolha saida do validador
            else:
                print("\nObrigado por utilizar o validador de CPF\n")
                break # Finalizando validador
        
        # Caso de uma escolha inválida pelo usuário
        except ValueError:
            print('Digite uma opção válida!') 

# Função de busca de arquivos JSON
def cpf_search():
    cpf_list = [] # Lista de CPFs para caso o usuário deseje salvar um arquivo JSON manualmente.

    while True:
        try:
            # Escolha do usuário
            choice = int(input('''Digite uma opção:

            [1] Salvar CPF manualmente
            [2] Buscar CPF
            [3] Sair do gerenciador
            
            Digite sua escolha: '''))

            # Escolha 1, salvar manualmente
            if choice == 1:
                archive = input('Digite um nome para o arquivo: ') + '.json' # Pergunta ao usuário um nome de arquivo para salvar o JSON
                
                program_continue = 'S' # Variavel de controle
                while program_continue == 'S': # Verficar se o While deve continuar

                    cpf = input('Digite o CPF: ') # Inserção do CPF pelo usuário
                    cpf_list.append(cpf)# Inserção do CPF na lista

                    program_continue = input('Deseja inserar um novo CPF? (S/N): ') # Resposta para váriavel de controle
                    program_continue = program_continue.upper() # Colocar reposta em CAPS

                # Mandando o nome do 'archive' escolhido pelo usuário e a lista de cpfs inseridos para função manager.save_json
                manager.save_json(archive, cpf_list) 
            
            # Escolha 2, Buscar arquivo JSON
            elif choice == 2:

                archive = manager.search_json() # Busca um arquivo JSON na função manager.search_json
                dados = manager.read_json(archive) # Lê o arquivo JSON encontrado usando função manager.read_json
                print('\nCPF do arquivo:')
                # Desempacota o arquivo JSON
                for CPF in dados:
                    print(CPF)
                print()

                # Tempo de espera para o programa continuar após 3 segundos 
                # para assim o usuário visualizar melhor os CPFs
                time.sleep(3)

            # Escolha de fechar programa
            else:
                print("\nObrigado por utilizar o gerenciador de CPF\n")
                break # Encerra o buscador de JSON

        # Caso de uma escolha inválida pelo usuário
        except ValueError:
            print('Digite uma opção válida!') 



while True:
    try:
        # Escolha inicial do usuário
        choice = int(input('''Digite uma opção:

        [1] Gerador de CPFs
        [2] Validador de CPFs
        [3] Gerenciador de arquivos CPFs
        [4] Fechar o programa

        Digite sua escolha: '''))

        # Escolha 1, Gerador CPF
        if choice == 1:
            cpf_generator() # Manda para função de gerador de CPF

        # Escolha 2, Validador
        elif choice == 2:
            cpf_validator() # Manda para função de validador de CPF

        # Escolha 3 Gerenciador
        elif choice == 3:
            cpf_search() # Manda para o gerenciador de CPFs
        
        # Caso o usuário deseja sair do programa
        else:
            print('Obrigado por utilizar o programa!')
            break # Finaliza todo o programa
    
    # Caso de uma escolha inválida pelo usuário
    except ValueError:
        print('Digite um valor válido!')