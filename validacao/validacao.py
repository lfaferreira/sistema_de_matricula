class Validacao:
    def __init__(self):
        self.__LIMITE_PRIMEIRA_VALIDACAO = 10
        self.__LIMITE_SEGUNDA_VALIDACAO = 11
        self.__INDICE_CPF_PRIMEIRA_VALIDACAO = 9
        self.__INDICE_CPF_SEGUNDA_VALIDACAO = 10
        self.__CPFS_INVALIDOS = ['00000000000',
                                 '11111111111',
                                 '22222222222',
                                 '33333333333',
                                 '44444444444',
                                 '55555555555',
                                 '66666666666',
                                 '77777777777',
                                 '88888888888',
                                 '99999999999']

    def valida_cpf(self, cpf):
        cpf = self.__formata_cpf(cpf)
        if self.__valida_tamanho_cpf(cpf) and self.__não_eh_cpfs_invalidos(cpf):
            cpf_multiplicado = self.__multiplica_cpf(cpf, self.__LIMITE_PRIMEIRA_VALIDACAO)
            if self.__valida_divisão_do_cpf_multiplicado(cpf_multiplicado, cpf, self.__INDICE_CPF_PRIMEIRA_VALIDACAO):
                cpf_multiplicado = self.__multiplica_cpf(cpf, self.__LIMITE_SEGUNDA_VALIDACAO)
                return self.__valida_divisão_do_cpf_multiplicado(cpf_multiplicado, cpf, self.__INDICE_CPF_SEGUNDA_VALIDACAO)
        return False

    def __formata_cpf(self, cpf):
        return cpf.replace('.','').replace('-','').strip()

    def __valida_tamanho_cpf(self, cpf):
        return True if len(cpf) == 11 else False

    def __não_eh_cpfs_invalidos(self, cpf):
        for value in self.__CPFS_INVALIDOS:
            if cpf == value:
                return False
        return True

    def __multiplica_cpf(self, cpf, limite):
        valor = 0
        indice = 0
        for digito in range(limite, 1, -1):
            valor = valor + (digito * int(cpf[indice]))
            indice+=1
        return valor

    def __valida_divisão_do_cpf_multiplicado(self, cpf_multiplicado, cpf, indice):
        resto = abs((cpf_multiplicado*10)%11)
        if resto == 10:
            resto = 0
        return resto == int(cpf[indice])