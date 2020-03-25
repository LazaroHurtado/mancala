from gameLogic import Mancala

# main method for when playing the game
def playGame():
    # player one's name
    player_one = input('>> Player one name: ')
    # player two's name
    player_two = input('>> Player two name: ')
    # asign the pit letters to each player
    player_pits = {player_one:'A', player_two:'B'}
    # instantiate the main game logic class
    gameClass = Mancala()
    # keep track of the current player
    current_player = player_one
    # infinite loop for playing the game
    while True:
        # print whos turn it is
        pit_choosen = input(f">> {current_player}'s turn: ")
        # get the pit letter of the current player
        player_letter = player_pits[current_player]
        # if the pit choosen is valid play it
        if gameClass.valid_pit(pit_choosen, player_letter):
            # pass the stones of the choosen pit around and check if the player
            # should go again
            go_again = gameClass.player_pit(pit_choosen, player_letter)
            # if the player doesn't go again then change the current player else don't
            if not go_again:
                # change current player
                current_player = (player_one) if current_player == player_two else player_two
        # if the pit is not valid print error statement
        else:
            print('>> Invalid option, try again')

# starting statements
print('>> Welcome to Mancala!')
print(">> To start enter 'start_game'")
print(">> For game instruction enter 'game_help'")

# get user input
userInput = input('>> ')

# start game
if userInput == 'start_game':
    playGame()
