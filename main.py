from models.fila_prioridade_model import FilaPrioridade
from models.professor_model import Professor


if __name__ =='__main__':
    prioridade = FilaPrioridade()
    
    prioridade.push(Professor('Bruno12', 554543,'drrdf', 'jjj', 'hhh', 12, 12,12))

    prioridade.push(Professor('Bruno15', 554545,'drrdf', 'jjj', 'hhh', 15, 12,12))

    prioridade.push(Professor('Bruno13', 554541,'drrdf', 'jjj', 'hhh', 13, 12,12))

    prioridade.push(Professor('Bruno10', 554540,'drrdf', 'jjj', 'hhh', 10, 12,12))

    prioridade.pop()

    prioridade.pop()

  
    print(prioridade.posicao_professor())
    print(prioridade)
    
    
