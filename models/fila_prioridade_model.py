



class FilaPrioridade:
    def __init__(self):
        self.__lista_professores = []


    #lista_professores
    @property
    def lista_professores(self):
        return self.__lista_professores


    #verifica se a lista de professores está vazia
    def empty(self):
        if len(self.__lista_professores) == 0:
            return True
        else:
            return False


    #adiciona o professor na lista e coloca-o na posição correta de acordo com o tempo de ifce caso a matricula dele não esteja na lista atual
    def push(self, professor):
        #verrificando se a matricula já está em uso
        ja_matriculado = False
        for prof in self.__lista_professores:
            if prof.matricula == professor.matricula:
                ja_matriculado = True
                print(f'A matricula já está em uso, não foi possível adicionar {professor.nome}')
        if ja_matriculado == False:
            self.__lista_professores.append(professor)
            self.__lista_professores = sorted(self.__lista_professores , key= lambda professor: professor.tempo_de_ifce, reverse= True)
    

    #remove o primeiro da lista de prioridade
    def pop(self):
        if self.empty():
            print('Sem elementos, impossível remover algo')
        else:
            self.__lista_professores.remove(self.__lista_professores[0])
    

    #retorna a quantidade de professores que fazem parte do campus
    def quantidade_professores(self):
        return len(self.__lista_professores)

    
    #informa em qual posição da lista de prioridades aquele professor se encontra
    def posicao_professor(self):
        if self.empty():
            return ('Nosso campus não possui nenhum professor.')
            
        else:
            while True:
                console = input('Digite a matrícula do professor : ')
                try:
                    matricula = int(console)
                    index = -1
                    for professor in self.__lista_professores:
                        index += 1
                        if professor.matricula == matricula:
                            return f'\nO(a) professor(a) {professor.nome} é o(a) {index + 1}º na lista de prioridade'
                    print('Matrícula inválida, digite outra')
                except:
                    print('Digite um valor inteiro por favor!')

                
    #imprime a lista de prioridade
    def __str__(self):
        if self.empty():
            return 'sem elementos'
        string_final = ''
        
        for professor in self.__lista_professores:

            string_final = string_final + f'{professor.nome} prioridade: {professor.tempo_de_ifce}'
            if professor != self.lista_professores[-1]:
                string_final += '\n'
            
        return string_final
       
   