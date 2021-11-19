def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number -1) + fibonacci(number -2)

def palindromo(sentence):
        """ Retornar Verdadero si el parametro es un palindromo
        en caso contrario retorna falso

        sentence -- String o entero

        >>> palindromo("anita lava la tina")
        True
        """
        sentence = str(sentence).lower().replace(" ", "")
        return sentence == sentence[::-1]