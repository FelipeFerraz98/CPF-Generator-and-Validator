import json # Importa biblioteca JSON
import glob # Importa biblioteca glob


# Função para salvar arquivos JSON
def save_json(FILE_PATH, data):
    with open(FILE_PATH, 'w+', encoding='utf8') as archive:
        data = json.dump(data, archive, ensure_ascii=False, indent=2)
        # Salva os dados em formato JSON no arquivo especificado
        # A opção ensure_ascii=False garante que os caracteres não ASCII sejam salvos corretamente
        # O parâmetro indent=2 define a indentação de 2 espaços para melhor legibilidade

# Função para procurar arquivos JSON
def search_json():

    list_json = [] # Lista de arquivos json encontrados
    json = '*.json' # Especifica o que o programa deve buscar, no caso todos os arquivos finalizados com .json
    archives_json = glob.glob(f"{json}") # Busca todos os arquivos com final .json

    # Caso encontre arquivos JSON
    if archives_json:
        print('Lista de arquivos localizados: \n') # Pede para o usuário escolher um arquivo

        for index, archive in enumerate(archives_json):
            list_json.append(archive) # Adiciona todos os arquivos JSON encontrados em uma lista
            print(f'[{index+1}] {archive}') # Mostra a lista encontrada

    # Caso não localize arquivos JSON    
    else:
        print('Nenhum arquivo localizado!')

    while True:
        try:
            # Escolha de arquivs do usuário
            choice = int(input('Escolha um arquivo de senhas: '))

            if choice < 1: # Caso o usuário digite 0 para escolha
                print('Digite um valor maior ou igual a 1')
            break

        # Caso usuário digite um valor inválido
        except ValueError:
            print('\n Digite um valor válido!\n')

    return list_json[choice-1] # Retorna o arquivo escolhido pelo usuário
            

# Função para ler arquivo JSON
def read_json(FILE_PATH):
    with open(FILE_PATH, 'r', encoding='utf8') as archive:
        data = json.load(archive) # Carrega os dados do arquivo JSON
    return data # Retorna os dados carregados do arquivo JSON
     