# Exercício 1

print('Hello world.\n')

var1 = float(input('Digite um valor: '))
banana = float(input('Digite outro valor: '))

soma = var1 + banana

resto = soma % 2

print ('O resultado da soma é', soma)

if ( (var1 + banana) % 2 == 0):
    print('e ela é PAR.')

else:
    print('e ela é ÍMPAR.')