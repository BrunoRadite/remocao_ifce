class Professor:
    def __init__(self, nome, matricula,subarea, campus_atual, campus_removido,tempo_de_ifce,idade, nota_concurso):
        self.__nome = nome
        self.__matricula = matricula
        self.__subarea = subarea
        self.__campus_atual = campus_atual
        self.__campus_removido = campus_removido
        self.__tempo_de_ifce = tempo_de_ifce
        self.__idade = idade
        self.__nota_concurso = nota_concurso

    #nome
    @property
    def nome(self):
        return self.__nome 
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    #matricula
    @property
    def matricula(self):
        return self.__matricula 
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor
    
    #subarea
    @property
    def subarea(self):
        return self.__subarea 
    @subarea.setter
    def subarea(self, valor):
        self.__subarea = valor

    #campus_atual
    @property
    def campus_atual(self):
        return self.__campus_atual 
    @campus_atual.setter
    def campus_atual(self, valor):
        self.__campus_atual = valor

    #campus_removido
    @property
    def campus_removido(self):
        return self.__campus_removido 
    @campus_removido.setter
    def campus_removido(self, valor):
        self.__campus_removido = valor

    #tempo_de_ifce
    @property
    def tempo_de_ifce(self):
        return self.__tempo_de_ifce 
    @tempo_de_ifce.setter
    def tempo_de_ifce(self, valor):
        self.__tempo_de_ifce = valor

    #idade
    @property
    def idade(self):
        return self.__idade 
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    #nota_concurso
    @property
    def nota_concurso(self):
        return self.__nota_concurso 
    @nota_concurso.setter
    def nota_concurso(self, valor):
        self.__nota_concurso = valor
    
    def __str__(self):
        return self.__nome
    
    def __repr__(self):
        return repr((self.__nome, self.__matricula ,self.__tempo_de_ifce))

    