class Pessoa:
    def __init__(self, nome, cpf, data_de_nascimento, genero, telefone, email, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_de_nascimento = data_de_nascimento
        self.__genero = genero
        self.__lista_de_telefone = [telefone]
        self.__email = email
        self.__endereco = endereco


    def __getitem__(self, item):
        return self.__lista_de_telefone[item]

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @property
    def genero(self):
        return self.__genero

    @property
    def lista_de_telefone(self):
        return self.__data_de_nascimento

    @property
    def email(self):
        return self.__email

    @property
    def endero(self):
        return self.__endereco