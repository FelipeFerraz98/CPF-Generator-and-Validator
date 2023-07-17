from digit import DigitGenerator

# Função do algoritmo validador de CPFs
class AlgorithmValidator():
    def __init__(self, cpf: str) -> None:
        self._cpf = cpf
        self._cpf_new: str = '' # Variavel para armazenar o CPF com os dois digitos gerados a partir do algoritmo
        self._auth_count: int = 0 # Variavel para contar a quantidade de digitos iguais

    @property
    def validator(self) -> bool:
        for index in range(0,10):
            if self._cpf[index] == self._cpf[index+1]: # Verificando se o digito atual é igual o seu sucessor
                self._auth_count += 1 # Se for igual ao sucessor adiciona um ao auth_count

        # Caso o auth_cont seja igual a 10 o cpf inteiro é formado por numeros repetidos
        if self._auth_count == 10:
            return False # Retorna False para CPF inválido e acaba a verificação.
    
        for index in range(9):
            self._cpf_new += self._cpf[index] # Insere os 9 primeiros digitos do cpf na variavel cpf_new
        

        # Laço de repetição para o calculo dos 2 ultimos digitos do CPF
        for index in range(10,12):
            d = DigitGenerator(self._cpf_new)
            # Coloca o valor da multiplicação na função digit_generator
            self._cpf_new += d.digit_generator(index) 
            # Pega o resultado da função digit_generator e insere na variavel cpf_generated

        # Caso a variavel cpf_new seja igual ao cpf inserido o CPF é válido
        if self._cpf_new == self._cpf:
            return True # Retorna True
        
        # Caso a variavel cpf_new seja diferente do cpf inserido o CPF é inválido
        else:
            return False # Retorna False