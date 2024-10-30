import random

options = ['piedra', 'papel', 'tijera']

def get_player_choice():
    while True:
        player = input('Elige piedra, papel o tijera: ').lower()

        if player in options:
            return player
            
        print('Elige una opcion valida')
           
def get_computer_choice():
    return random.choice(options)


def determine_winner(player, computer):
    if player == computer:
        return 'empate!'
    elif (player == 'piedra' and computer == 'tijera') or \
         (player == 'tijera' and computer == 'papel') or \
         (player == 'papel' and computer == 'piedra'):
         return 'Ganaste'
    else:
        return 'perdiste'

def play_again():
    jugar_de_nuevo = input('Quieres jugar de nuevo? (si/no): ').lower()

    return jugar_de_nuevo == 'si'


def play_game():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()

        print(f'La computadora eligo: {computer}')
        result = determine_winner(player, computer)
        print(result)

        if not play_again():
            print('Gracias por jugar!')
            break

play_game()       


    
    

              
    