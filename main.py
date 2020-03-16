from gameLogic import Mancala

def playGame():
    player_one = input('>> Player one name: ')
    player_two = input('>> Player two name: ')
    player_pits = {player_one:'A', player_two:'B'}
    gameClass = Mancala()
    current_player = player_one
    while True:
        pit_choosen = input(f">> {current_player}'s turn: ")
        player_letter = player_pits[current_player]

        if gameClass.valid_pit(pit_choosen, player_letter):
            go_again = gameClass.player_pit(pit_choosen, player_letter)
            if not go_again:
                current_player = (player_one) if current_player == player_two else player_two


        else:
            print('>> Invalid option, try again')


print('>> Welcome to Mancala!')
print(">> To start enter 'start_game'")
print(">> For game instruction enter 'game_help'")

userInput = input('>> ')

if userInput == 'start_game':
    playGame()
