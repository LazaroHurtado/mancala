from gameLogic import Mancala

valid_pits = {'A1','A2','A3','A4','A5','A6','B1','B2','B3','B4','B5','B6'}

def playGame():
	player_one = input('>> Player one name: ')
	player_two = input('>> Player two name: ')
	player_pits = {player_one:'A', player_two:'B'}
	gameClass = Mancala()
	current_player = player_one
	while True:
		print(">> "+current_player+"'s turn")
		pit_choosen = input('>> Choose a pit: ')
		if pit_choosen in valid_pits:
			if pit_choosen[0] == player_pits[current_player]:
				play_again = gameClass.player_pit(pit_choosen, player_pits[current_player])
				if current_player == player_one and not play_again:
					print('hi')
					current_player = player_two
				elif current_player == player_two and not play_again:
					print('hi')
					current_player = player_one
			else:
				print('>> You can not choose that pit, try again')
		else:
			print('>> Invalid option, try again')


print('>> Welcome to Mancala!')
print(">> To start enter 'start_game'")
print(">> For game instruction enter 'game_help'")

userInput = input('>> ')

if userInput == 'start_game':
	playGame()
