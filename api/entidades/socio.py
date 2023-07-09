class Socio():
    def __init__(self, nome, idade, plano):
        self.__nome = nome
        self.__idade = idade
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, novo_plano):
        self.__plano = novo_plano
