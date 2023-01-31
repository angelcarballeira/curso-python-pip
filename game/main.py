import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
    print('')

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('')
    print('Computadora', computer_wins)
    print('Usuario', user_wins)
    print('')

    user_option = input('piedra, papel o tijera => ').lower()

    rounds += 1

    if not user_option in options:
        print('Esa opción no es válida')
        print('')
        continue

    computer_option = random.choice(options)

    print('')

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Usuario gano!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Computadora gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Usuario gano!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Computadora gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Usuario gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computadora gano!')
            computer_wins += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break

    if user_wins == 2:
        print('El ganador es el usuario')
        break
