from classEstudante import Estudante
from classTrabalhador import Empregado

# class carro extends Veículo implements Movimento

class EstudanteTrabalhador(Estudante, Empregado):
    def __init__(self, nome, nomeEscola, nomeEmpresa):
        stress = True
        Estudante.__init__(self, nome, nomeEscola)
        Empregado.__init__(self, nomeEmpresa)

    def tomarCafé():
        return 'Tomando Café'