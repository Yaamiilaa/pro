""" def game(move_player1 = input('Elige un movimiento [Piedra, papel o tijera]: ').upper(), move_player2 ): """
move_player1 = input('Elige un movimiento [Piedra, papel o tijera]: ').upper()
move_player2 = input('Elige un movimiento [Piedra, papel o tijera]: ').upper()

if move_player1 == 'PIEDRA' and move_player2 == 'PIEDRA':
    print('Empate')
elif move_player1 == 'PIEDRA' and move_player2 == 'PAPEL':
    print('Gana el jugador 2')
elif move_player1 == 'PIEDRA' and move_player2 == 'TIJERA':
    print('Gana el jugador 1')   
elif move_player1 == 'PAPEL' and move_player2 == 'PIEDRA':
    print('Gana el jugador 1')
elif move_player1 == 'PAPEL' and move_player2 == 'PAPEL':
    print('Empate')
elif move_player1 == 'PAPEL' and move_player2 == 'TIJERA':
    print('Gana el jugador 2')
elif move_player1 == 'TIJERA' and move_player2 == 'PIEDRA':
    print('Gana el jugador 2')
elif move_player1 == 'TIJERA' and move_player2 == 'PAPEL':
    print('Gana el jugador 1')
elif move_player1 == 'TIJERA' and move_player2 == 'TIJERA ':
    print('Empate')