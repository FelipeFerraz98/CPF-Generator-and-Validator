import random

def algorithm_generator():
    random_number = []
    for _ in range(9):
        random_number.append(random.randint(0,9))


    def digit_generator(multiply):
        digit = 0
        for number in random_number:
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

        random_number.append(digit)


    for index in range(10,12):
        digit = digit_generator(index)
        digit_calculation(digit)

    cpf = ''
    for number in random_number:
        cpf += str(number)

    return cpf
