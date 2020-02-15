from gameLogic import Mancala

def playGame():
	player_one = input('>> Player one name: ')
	player_two = input('>> Player two name: ')
	gameClass = Mancala()

print('>> Welcome to Mancala!')
print(">> To start enter 'start_game'")
print(">> For game instruction enter 'game_help'")

userInput = input('>> ')

if userInput == 'start_game':
	playGame()
