from classPessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nomeEscola, nomePessoa):        
        self.nomeEscola = nomeEscola 
        super().__init__(nomePessoa)