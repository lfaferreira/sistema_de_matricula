import re

#Codigo do validacao_cpf é do "Woss" e está no stackoverflow, link https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf

def validacao_cpf(cpf: str) -> bool:

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validacao_cpf('529.982.247-25')
    True
    >>> validacao_cpf('52998224725')
    False
    >>> validacao_cpf('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def validacao_nome(nome_inserido: str) -> str:

    """ Efetua a validação do nome, tanto formatação quando caracteres verificadores.

    Parâmetros:
        nome_inserido (str): Nome a ser validado

    Retorno:
        str:
            - "Nome invalido", quando a string não formada apenas por letras
            - Nome formatado (retira excesso de espaços e coloca cada primeira letra maiscula), quando a string contem apenas letras

    Exemplos:

    >>> validacao_nome('              Enalde         Pereira      ')
    'Enalde Pereira'
    >>> validacao_nome('52998224725')
    'Nome Invalido'
    >>> validacao_nome('][]~~ç/;´çl')
    'Nome Invalido'
    >>> validacao_nome('Iêda Ágnes')
    'Iêda Ágnes'
    """

    for digito in nome_inserido.split():
        if not digito.isalpha():
            return 'Nome Invalido'

    nome_seprado = nome_inserido.title().split()
    nome = ''
    for posicao in range(0, len(nome_seprado)):
        nome += nome_seprado[posicao] + ' ' if posicao < len(nome_seprado)-1 else nome_seprado[posicao]

    return nome

def validacao_telefone(telefone_inserido: str) -> str:

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validacao_telefone('529.982.247-25')
    'Telefone Invalido'
    >>> validacao_telefone('pedroMracos')
    'Telefone Invalido'
    >>> validacao_telefone('11111199')
    'Tamanho do Numero Invalido'
    >>> validacao_telefone('81995329479')
    '81995329479'
    """

    for digito in telefone_inserido:
        if not digito.isdigit():
            return 'Telefone Invalido'

    if len(telefone_inserido) < 10:
        return 'Tamanho do Numero Invalido'

    return telefone_inserido
