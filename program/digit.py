class DigitGenerator():
    def __init__(self, cpf) -> None:
        self._cpf = cpf

        # Função para calcular um digito válido para o final do CPF
    def digit_generator(self, multiply: int) -> str:
        digit = 0 # Digito inicia em 0 para manter valor limpo
        # Desempacota lista de numeros
        for index in range(len(self._cpf)):
            number = int(self._cpf[index]) # Pega um numero do CPF
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