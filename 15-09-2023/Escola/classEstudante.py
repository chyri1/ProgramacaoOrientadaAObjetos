from classPessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, númeroMatrícula, notas, nomePessoa, idadePessoa, endereçoPessoa):
        self.númeroMatrícula = númeroMatrícula
        self.notas = notas
        super().__init__(nomePessoa, idadePessoa, endereçoPessoa)