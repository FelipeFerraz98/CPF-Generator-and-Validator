import random # Importa biblioteca random

# Função do algoritmo gerador de CPFs
def algorithm_generator():
    cpf_generated = '' # Lista para inserir os numeros do CPF
    for _ in range(9):
        cpf_generated += str(random.randint(0,9)) # Insere numeros aleatórios no CPF
 

    # Função para calcular um digito válido para o final do CPF
    def digit_generator(multiply):
        digit = 0 # Digito inicia em 0 para manter valor limpo
        # Desempacota lista de numeros
        for index in range(len(cpf_generated)):
            number = int(cpf_generated[index]) # Pega um numero do CPF
            digit += number * multiply # Soma a multiplicação de um digito do CPF
            multiply -= 1 # Diminui um na multiplicação

        # Caso o resto da divisão do digito por 11 seja menor que 2 atribui 0
        if digit % 11 < 2:
            digit = 0

        # Caso o resto da divisão do digito por 11 seja maior que 2
        else:
            digit = digit % 11 # Pega o valor do resto da divisão por 11
            digit -= 11 # Subtrai 11 do resto da divisão
            digit = abs(digit) # Coloca o resultado em valor absoluto

        return str(digit) # Retorna o digito calculado

    # Laço de repetição para o calculo dos 2 ultimos digitos do CPF
    for multiply in range(10,12):
        # Coloca o valor da multiplicação na função digit_generator
        cpf_generated += digit_generator(multiply) 
        # Pega o resultado da função digit_generator e insere na variavel cpf_generated


    return cpf_generated # Retorna variavel cpf_generated
