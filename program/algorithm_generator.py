import random # Importa biblioteca random
from digit import DigitGenerator

# Função do algoritmo gerador de CPFs
class AlgorithmGenerator():
    def __init__(self) -> None:
        self._cpf_generated = ''
        for _ in range(9):
            self._cpf_generated += str(random.randint(0,9)) # Insere numeros aleatórios na string CPF

    @property
    def generator(self):
        # Laço de repetição para o calculo dos 2 ultimos digitos do CPF
        for multiply in range(10,12):
            d = DigitGenerator(self._cpf_generated)
            # Coloca o valor da multiplicação na função digit_generator
            self._cpf_generated += d.digit_generator(multiply) 
            # Pega o resultado da função digit_generator e insere na variavel cpf_generated


        return self._cpf_generated # Retorna variavel cpf_generated