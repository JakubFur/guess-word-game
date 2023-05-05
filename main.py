from logic import *

game = 0
difficult = 0

while (game != 3):
    print('Co robimy szefie?')
    print('1. Nowa gra.')
    print('2. Losuj słowo')
    print('3. Koniec')
    game = input()
    if game == '1':
        print(guess_the_word())
        print()
        continue
    elif game == '2':
        # ZMIANA POZIOMU TRUDNOŚCI!
        print(draw_a_word())
        print()
        continue
    elif game == '3':
        break
    else:
        print('Nieprawidłowa wartość wyboru. Chuj.')
        print()