class Carro:

    def __init__(self, marca, modelo, cor, velmax):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velmax = velmax
        self.comCombustível = True

    def acelerar():
        print('Acelerando muito aqui')

    def frear():
        print('Freando')

    def zerandoCombustível(self):
        self.comCombustível = False

fiatUno = Carro('Fiat', 'Uno', 'Preto', 100)

print(f' O modelo do carro é {fiatUno.marca} {fiatUno.modelo}.')

# car = Carro()
# gol = Carro()
# ferrari = Carro()

# carro1.modelo = 'Uno'
# carro1.marca = 'Fiat'
# carro1.copr = 'Preto'
# carro1.velmax = 100

# ferrari.acelerar()
# gol.acelerar()
# carro1.acelerar()
