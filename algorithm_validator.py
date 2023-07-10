def algorithm_validator(cpf):
    cpf_new = ''
    for index in range(9):
        cpf_new += cpf[index]

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
    