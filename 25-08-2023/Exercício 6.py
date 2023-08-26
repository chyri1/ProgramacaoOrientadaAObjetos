class Pessoa:

    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.apresentando = True

    def apresentar():
        print('Meu nome é {self.nome}.')

ana = Pessoa('Ana', 20, 'Sorocaba')

print(f' O nome dela é {ana.nome}.')