import random # Importa biblioteca random

# Função do algoritmo gerador de CPFs
def algorithm_generator():
    random_number = [] # Lista para inserir os numeros do CPF
    for _ in range(9):
        random_number.append(random.randint(0,9)) # Insere numeros aleatórios no CPF
 

    # Função para calcular um digito válido para o final do CPF
    def digit_generator(multiply):
        digit = 0 # Digito inicia em 0 para manter valor limpo
        # Desempacota lista de numeros
        for number in random_number:
            digit += number * multiply # Soma a multiplicação de um digito do CPF
            multiply -= 1 # Diminui um na multiplicação
        return digit # Retorna o digito

    # Calcula o valor final do digito
    def digit_calculation(digit):

        # Caso o resto da divisão do digito por 11 seja menor que 2 atribui 0
        if digit % 11 < 2:
            digit = 0

        # Caso o resto da divisão do digito por 11 seja maior que 2
        else:
            digit = digit % 11 # Pega o valor do resto da divisão por 11
            digit -= 11 # Subtrai 11 do resto da divisão
            digit = abs(digit) # Coloca o resultado em valor absoluto

        random_number.append(digit) # Adiciona o digito a lista de digitos do CPF

    # Laço de repetição para o calculo dos 2 ultimos digitos do CPF
    for multiply in range(10,12):
        digit = digit_generator(multiply) # Coloca o valor da multiplicação na função digit_generator
        digit_calculation(digit) # Pega o resultado da função digit_generator e insere na função digit_calculation

    cpf = '' # Atribui str a variavel cpf
    # Desempacota os digitos do cpf da lista random_number
    for number in random_number:
        cpf += str(number) # Adiciona todos os digitos do CPF na variavel cpf

    return cpf # Retorna variavel cpf
