class Carro:

    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.cor = ''
        self.velmax = ''
        self.comCombustível = True

    def acelerar():
        print('Acelerando muito aqui')

    def frear():
        print('Freando')

    def zerandoCombustível(self):
        self.comCombustível = False

carro1 = Carro()
car = Carro()
gol = Carro()
ferrari = Carro()

print(f' O modelo do carro é {carro1.modelo}')