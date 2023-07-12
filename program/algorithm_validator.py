# Função do algoritmo validador de CPFs
def algorithm_validator(cpf):
    cpf_new = '' # Variavel para armazenar o CPF com os dois digitos gerados a partir do algoritmo
    auth_count = 0 # Variavel para contar a quantidade de digitos iguais

    for index in range(0,10):
        if cpf[index] == cpf[index+1]: # Verificando se o digito atual é igual o seu sucessor
            auth_count += 1 # Se for igual ao sucessor adiciona um ao auth_count

    # Caso o auth_cont seja igual a 10 o cpf inteiro é formado por numeros repetidos
    if auth_count == 10:
        return False # Retorna False para CPF inválido e acaba a verificação.
    
    for index in range(9):
        cpf_new += cpf[index] # Insere os 9 primeiros digitos do cpf na variavel cpf_new

    # Função para calcular um digito válido para o final do CPF
    def digit_generator(multiply):
        digit = 0# Digito inicia em 0 para manter valor limpo
        
        # Percorre todos os numeros do CPF
        for index in range(len(cpf_new)):
            number = int(cpf[index]) # Pega um numero do CPF
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
    for index in range(10,12):
        # Coloca o valor da multiplicação na função digit_generator
        cpf_new += digit_generator(index) 
        # Pega o resultado da função digit_generator e insere na variavel cpf_generated

    # Caso a variavel cpf_new seja igual ao cpf inserido o CPF é válido
    if cpf_new == cpf:
        return True # Retorna True
    
    # Caso a variavel cpf_new seja diferente do cpf inserido o CPF é inválido
    else:
        return False # Retorna False
    