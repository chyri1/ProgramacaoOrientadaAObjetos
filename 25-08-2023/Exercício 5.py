class Carro:

    def __init__(self, m1, pera, c1, banana):
        self.marca = pera
        self.modelo = m1
        self.cor = c1
        self.velmax = banana
        self.comCombustível = True

    def acelerar():
        print('Acelerando muito aqui')

    def frear():
        print('Freando')

    def zerandoCombustível(self):
        self.comCombustível = False

carro1 = Carro('Fiat', 'Uno', 'Preto', 100)
# car = Carro()
# gol = Carro()
# ferrari = Carro()

# carro1.modelo = 'Uno'
# carro1.marca = 'Fiat'
# carro1.copr = 'Preto'
# carro1.velmax = 100

print(f' O modelo do carro é {carro1.velmax}')
# ferrari.acelerar()
# gol.acelerar()
# carro1.acelerar()
