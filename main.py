from game_logic import GameLogic

def play_game(player_one, player_two):
    player_mapping = {player_one:"A", player_two:"B"}
    players_turn = player_one
    next_player = player_two
    playing = True
    game_logic = GameLogic(player_mapping)
    while playing:
        game_logic.show_board()
        choosen_pit = input(f"{players_turn}, choose a pit: ")
        if choosen_pit and game_logic.valid_pit(players_turn, choosen_pit):
            go_again = game_logic.move(players_turn, choosen_pit)
            if game_logic.game_ended(player_one, player_two):
                playing = False
            elif not go_again:
                players_turn, next_player = next_player, players_turn
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    player_one = input("Player one: ")
    player_two = input("Player two: ")
    play_game(player_one, player_two)
