# Função do algoritmo validador de CPFs
def algorithm_validator(cpf):
    cpf_new = '' # Variavel para armazenar o CPF com os dois digitos gerados a partir do algoritmo
    cpf_auth = [] # Lista para adicionar digito por digito e verificar se os digitos são iguais
    auth_count = 0 # Variavel para contar a quantidade de digitos iguais

    for index in range(11):
        cpf_auth.append(cpf[index]) # Inserindo os digitos na lista
    
    for index in range(0,10):
        if cpf_auth[index] == cpf_auth[index+1]: # Verificando se o digito atual é igual o seu sucessor
            auth_count += 1 # Se for igual ao sucessor adiciona um ao auth_count

    # Caso o auth_cont seja igual a 10 o cpf inteiro é formado por numeros repetidos
    if auth_count == 10:
        return False # Retorna False para CPF inválido e acaba a verificação.
    
    for index in range(9):
        cpf_new += cpf[index] # Insere os 9 primeiros digitos do cpf na variavel cpf_new

    
    def digit_generator(multiply):
        digit = 0

        for index in range(len(cpf_new)):
            number = int(cpf[index])
            digit += number * multiply
            multiply -= 1

        return digit

    def digit_calculation(digit):

        if digit % 11 < 2:
            digit = 0

        else:
            digit = digit % 11
            digit -= 11
            digit = abs(digit)

        return str(digit)


    for index in range(10,12):
        digit = digit_generator(index)
        cpf_new += digit_calculation(digit)

    if cpf_new == cpf:
        return True

    else:
        return False
    