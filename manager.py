import json
import glob


def save_json(FILE_PATH, data):
    with open(FILE_PATH, 'w+', encoding='utf8') as archive:
        data = json.dump(data, archive, ensure_ascii=False, indent=2)
        
def search_json():
    list_json = []
    index = 1
    json = '*.json'
    archives_json = glob.glob(f"{json}")
    if archives_json:
        print('Selecione um arquivo: \n')
        for archive in archives_json:
            list_json.append(archive)
            print(f'[{index}] {archive}')
            index += 1

    while True:
        try:
            choice = int(input('Escolha um arquivo de senhas: '))
            if choice < 1:
                print('Digite um valor maior ou igual a 1')
            break
        except ValueError:
            print('\n Digite um valor válido!\n')

    return list_json[choice-1]
            


def read_json(FILE_PATH):
    with open(FILE_PATH, 'r', encoding='utf8') as archive:
        data = json.load(archive)
    return data
    