menu = 0
while (menu !=4):
    print()
    print('Escolha uma opção: ')
    print('1 - Bom dia!')
    print('2 - Boa tarde!')
    print('3 - Boa noite!')
    print('4 - Sair.\n')
    menu = int(input('Digite uma opção: '))
    if(menu == 1):
        print('\nBom dia!')
    elif(menu == 2):
        print('\nBoa tarde!')
    elif(menu == 3):
        print('\nBoa noite!')
    elif(menu == 4):
        print('\nADEUS!')